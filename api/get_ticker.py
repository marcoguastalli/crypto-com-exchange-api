# url = https://api.crypto.com/v2/public/get-ticker
#       https://api.crypto.com/v2/public/get-ticker?instrument_name=XRP_USDT
# https://exchange-docs.crypto.com/spot/index.html#public-get-ticker

import json

import requests
from api.api_request import ApiRequest


class GetTicker(ApiRequest):
    def __init__(self, url):
        super().__init__(url, None, None)

    def do_get(self):
        response = None
        try:
            req = {
                "id": 1,
                "method": "public/get-ticker",
                "nonce": super().get_nonce()
            }
            headers = {'Content-type': 'application/json'}
            response = requests.get(self.url, headers=headers, data=json.dumps(req))

        except Exception as e:
            print("Error GetTicker:\n %s" % req)
            print(e)

        return response

    @staticmethod
    def parse_response(api_response: requests.models.Response):
        result: dict = {}

        json_response = api_response.json()
        json_response_result = json_response['result']
        data = json_response_result['data']
        for ticker in data:
            pair = ticker['i']
            result[pair] = ticker
        return result
