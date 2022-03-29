#!/usr/bin/env python3
import pyotp 
import robin_stocks as r
import inspect
from config import CONFIG, log
import sys
import string

class DataQuery:
    def __init__(self, CONFIG):
        self.login_message = self.robin_hood_login(CONFIG)

    query_for_stocks = lambda self, query: r.stocks.find_instrument_data(query)
    query_for_all_stocks = lambda self, letter: [stock["symbol"] for stock in self.query_for_stocks(letter) if stock["type"] == "stock"]

    def robin_hood_login(self, CONFIG: object) -> str:
        try:
            print("Logging into robinhood API...")
            two_factor_auth_code = pyotp.TOTP(CONFIG.RobinHood.authcode).now()
            r.login(CONFIG.RobinHood.user , CONFIG.RobinHood.password, mfa_code=two_factor_auth_code, store_session=False)
            return "login success"
        except Exception as e:
            return f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e)

    def alphabet_traversal_stock_search(self):
        stock_list = list()
        for letter in string.ascii_lowercase:
            for stock in self.query_for_all_stocks(letter):
                stock_list.append(stock)
        return stock_list



dq = DataQuery(CONFIG)
print(dq.login_message)
print(dq.alphabet_traversal_stock_search())

