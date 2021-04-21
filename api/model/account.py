class Account:

    def __init__(self, currency, balance, available, order, stake):
        self.__currency = currency
        self.__balance = balance
        self.__available = available
        self.__order = order
        self.__stake = stake

    def get_currency(self):
        return self.__currency

    def get_balance(self):
        return self.__balance

    def get_available(self):
        return self.__available

    def get_order(self):
        return self.__order

    def get_stake(self):
        return self.__stake

    def __str__(self):
        result = '{' \
                 + '"currency":"' + self.__currency + '",' \
                 + '"balance" :' + str(self.__balance) + ',' \
                 + '"available": ' + str(self.__available) + ',' \
                 + '"order": ' + str(self.__order) + ',' \
                 + '"stake": ' + str(self.__stake) \
                 + "}"
        return result
