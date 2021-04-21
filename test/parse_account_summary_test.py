import unittest

from app_cdc_account.api.model.account import Account


class Test(unittest.TestSuite):
    class Tests(unittest.TestCase):

        def test_get_account_list(self):
            json_str = """{
                          'id': 1,
                          'method': 'private/get-account-summary',
                          'code': 0,
                          'result': {
                            'accounts': [
                              {
                                'balance': 11,
                                'available': 22,
                                'order': 33,
                                'stake': 4,
                                'currency': 'EUR'
                              }
                            ]
                          }
                        }"""
            json_response = eval(json_str)
            json_response_result = json_response['result']
            accounts = json_response_result['accounts']
            self.assertIsNotNone(accounts)
            self.assertTrue(type(accounts) == list)

            for account in accounts:
                account = Account(account['currency'], account['balance'], account['available'], account['order'],
                                  account['stake'])
                print(account)


if __name__ == "__main__":
    unittest.main(Test)
