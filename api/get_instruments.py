# url = https://api.crypto.com/v2/public/get-instruments
# https://exchange-docs.crypto.com/spot/index.html#public-get-instruments

import json

import requests
from api.api_request import ApiRequest


class GetInstruments(ApiRequest):
    def __init__(self, url):
        super().__init__(url, None, None)

    def do_get(self):
        response = None
        try:
            req = {
                "id": 1,
                "method": "public/get-instruments",
                "nonce": super().get_nonce()
            }
            headers = {'Content-type': 'application/json'}
            response = requests.get(self.url, headers=headers, data=json.dumps(req))

        except Exception as e:
            print("Error GetInstruments:\n %s" % req)
            print(e)

        return response
