import uuid
import json

from .gateway import Gateway

class Device(Gateway):
    secure = True

    def create(self, username = 'default', token = None, type='default'):
        pathname = '/api/devices/'
        if not token:
            token = str(uuid.uuid4()).replace('-', '')

        return self.request(pathname, 'POST', data = {'username': username, 'token': token, 'type': type})

    def update_token(self, uuidOrToken, token):
        pathname = '/api/devices/{}/token/'.format(uuidOrToken)

        return self.request(pathname, 'POST', data = {'token': token})

    def update_type(self, uuidOrToken, type):
        pathname = '/api/devices/{}/type/'.format(uuidOrToken)

        return self.request(pathname, 'POST', data = {'type': type})

    def update_meta(self, uuidOrToken, meta):
        pathname = '/api/devices/{}/meta/'.format(uuidOrToken)

        if not isinstance(meta, str):
            meta = json.dumps(meta)

        return self.request(pathname, 'POST', data = {'meta': meta})

    def get_list(self, from_ = 0, size = 10, type = ''):
        pathname = '/api/devices/'
        return self.request(pathname, query={ 'from': from_, 'size': size, 'type': type })

    def get_list_by_user(self, username = 'default', from_ = 0, size = 10, type = ''):
        pathname = '/api/users/{}/devices/'.format(username)
        return self.request(pathname, query={ 'from': from_, 'size': size, 'type': type })

    def remove(self, uuidOrToken):
        pathname = '/api/devices/{}/'.format(uuidOrToken)

        return self.request(pathname, 'DELETE')

    def get(self, uuidOrToken):
        pathname = '/api/devices/{}/'.format(uuidOrToken)

        return self.request(pathname)

    def rpc(self, uuidOrToken, payload, timeout=300, format='json'):
        pathname = '/api/devices/{}/rpc/'.format(uuidOrToken)

        if not isinstance(payload, str):
            payload = json.dumps(payload)
        return self.request(pathname, 'POST', data={
            'payload': payload,
            'timeout': timeout,
            'format': format
        }, auto_pop=False)
