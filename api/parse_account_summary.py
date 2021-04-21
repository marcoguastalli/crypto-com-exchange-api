import requests

from api.model.account import Account


class ParseAccountSummary:
    def __init__(self, api_response: requests.models.Response):
        self.api_response = api_response

    def get_account_list(self):
        json_response = self.api_response.json()
        json_response_result = json_response['result']
        accounts = json_response_result['accounts']
        result: list = []
        for account in accounts:
            result.append(Account(account['currency'],
                                  account['balance'],
                                  account['available'],
                                  account['order'],
                                  account['stake']))
        return result
