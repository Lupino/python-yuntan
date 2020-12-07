import json
from datetime import datetime

from .gateway import Gateway


class Cart(Gateway):
    secure = True

    def add_product(self, username, product_id, num=1):
        pathname = '/api/cart/{}/'.format(username)
        return self.request(pathname,
                            'POST',
                            data={
                                'product_id': product_id,
                                'num': num,
                            })

    def get_cart(self, username):
        pathname = '/api/cart/{}/'.format(username)
        return self.request(pathname)

    def remove_product(self, username, product_id):
        pathname = '/api/cart/{}/'.format(username)
        return self.request(pathname,
                            'DELETE',
                            data={'product_id': product_id})

    def create_order(self,
                     username,
                     amount,
                     body={},
                     order_sn=None,
                     status='created'):
        pathname = '/api/orders/'
        body = json.dumps(body)
        if not order_sn:
            order_sn = datetime.now().strftime('%Y%m%d%H%M%S')
        return self.request(pathname,
                            'POST',
                            data={
                                'username': username,
                                'amount': amount,
                                'body': body,
                                'order_sn': order_sn,
                                'status': status
                            })

    def update_order_status(self, orderIdOrSN, status):
        pathname = '/api/orders/{}/status/{}/'.format(orderIdOrSN, status)
        return self.request(pathname, 'POST', data={'none': 'none'})

    def update_order_body(self, orderIdOrSN, body):
        pathname = '/api/orders/{}/body/'.format(orderIdOrSN)
        body = json.dumps(body)
        return self.request(pathname, 'POST', data={'body': body})

    def update_order_amount(self, orderIdOrSN, amount):
        pathname = '/api/orders/{}/amount/'.format(orderIdOrSN)
        return self.request(pathname, 'POST', data={'amount': amount})

    def get_order_list(self, username=None, status=None, from_=0, size=10):
        pathname = '/api/orders/'
        if username and status:
            pathname = '/api/orders_by/user/{}/status/{}'.format(
                username, status)
        elif username:
            pathname = '/api/orders_by/user/{}/'.format(username)
        elif status:
            pathname = '/api/orders_by/status/{}/'.format(status)

        return self.request(pathname, query={'from': from_, 'size': size})

    def get_order(self, orderIdOrSN):
        pathname = '/api/orders/{}/'.format(orderIdOrSN)
        return self.request(pathname)

    def remove_order(self, orderIdOrSN):
        pathname = '/api/orders/{}/'.format(orderIdOrSN)
        return self.request(pathname, 'DELETE')
