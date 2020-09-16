import hmac
import hashlib
from time import time
from urllib.parse import urlencode
import json
import aiohttp


class ErrorResponse(Exception):
    pass


def to_byte(s):
    if isinstance(s, str):
        return bytes(s, 'utf-8')
    elif isinstance(s, bytes):
        return s
    else:
        return bytes(str(s), 'utf-8')


def sign_params(secret, params):
    m = hmac.new(to_byte(secret), digestmod=hashlib.sha256)
    update_json(m, params)

    return m.hexdigest().upper()


def update_json(m, params):
    if isinstance(params, list):
        for param in params:
            update_json(m, param)

    elif isinstance(params, dict):
        params = sorted(params.items(), key=lambda x: x[0])
        for k, v in params:
            m.update(to_byte(k))
            update_json(m, v)

    elif isinstance(params, bool):
        if params:
            m.update(b'true')
        else:
            m.update(b'false')
    else:
        m.update(to_byte(params))


class Gateway(object):
    secure = False

    def __init__(self, host, key, secret):
        self._host = host
        self._key = key
        self._secret = secret

    def get_headers(self, pathname='', params={}, secure=True):
        if secure:
            params = params.copy()
            params['key'] = self._key
            params['timestamp'] = str(int(time()))
            params['pathname'] = pathname
            sign = sign_params(self._secret, params)
            return {
                'X-REQUEST-KEY': self._key,
                'X-REQUEST-SIGNATURE': sign,
                'X-REQUEST-TIME': params['timestamp']
            }
        else:
            return {
                'X-REQUEST-KEY': self._key,
            }

    def get_uri(self, pathname, query=None):
        if query is None:
            return '{}{}'.format(self._host, pathname)
        else:
            return '{}{}?{}'.format(self._host, pathname, urlencode(query))

    async def request(self,
                      pathname,
                      method='GET',
                      query=None,
                      data=None,
                      headers={},
                      is_json=False,
                      auto_pop=True):
        params = {}
        if query:
            params.update(query.copy())
        if method != 'GET' or method != 'DELETE':
            if not data:
                data = {'none': 'none'}
        if data:
            params.update(data.copy())

        secure = True
        method = method.upper()
        if method == 'GET' and not self.secure:
            secure = False

        headers = self.get_headers(pathname, params, secure)
        if is_json:
            data = json.dumps(data)
            headers['content-type'] = 'application/json'

        headers['accept'] = 'application/json'
        url = self.get_uri(pathname, query)

        async with aiohttp.ClientSession() as client:
            async with client.request(method, url, headers=headers,
                                      data=data) as rsp:
                content = await rsp.read()

                try:
                    data = json.loads(str(content, 'utf-8'))
                    if data.get('err'):
                        raise ErrorResponse(data['err'])
                    if len(data.keys()) == 1 and auto_pop:
                        return list(data.values()).pop()
                    return data
                except json.decoder.JSONDecodeError:
                    raise ErrorResponse(content)
