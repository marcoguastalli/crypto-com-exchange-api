import time

from api.utils.sign_request import sign_request


class ApiRequest:
    def __init__(self, url, api_key, secret_key):
        self.url = url
        self.api_key = api_key
        self.secret_key = secret_key

    @staticmethod
    def get_nonce():
        return int(time.time() * 1000)

    def sign_request(self, req):
        return sign_request(req, self.api_key, self.secret_key)
