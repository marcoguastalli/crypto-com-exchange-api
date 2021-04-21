# url = https://api.crypto.com/v2/private/get-account-summary
# https://exchange-docs.crypto.com/spot/index.html#private-get-account-summary

import json
import time

import requests
from api.api_request import ApiRequest

from .utils.sign_request import sign_request


class GetAccountSummary(ApiRequest):
    def __init__(self, url, api_key, secret_key):
        super().__init__(url, api_key, secret_key)

    def do_post(self):
        response = None
        try:
            req = {
                "id": 1,
                "method": "private/get-account-summary",
                "api_key": self.api_key,
                "params": {},
                "nonce": int(time.time() * 1000)
            }
            req = sign_request(req, self.api_key, self.secret_key)
            if req is not None:
                headers = {'Content-type': 'application/json'}
                response = requests.post(self.url, headers=headers, data=json.dumps(req))
            else:
                return "Invalid req"

        except Exception as e:
            print("Error GetAccountSummary:\n %s" % req)
            print(e)

        return response
