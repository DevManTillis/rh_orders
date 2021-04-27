#!/usr/bin/env python3
# from RobinHood import buy_crypto, sell_crypto, robin_hood_login, get_available_cash_amount, get_crypto_usd_value, is_trade_window
from config import CONFIG
from RobinHood import robin_hood_login
# # TASKS
# #[x] Login
# #[x] Get current avaiable cash
# #[x] If buy action
# #    [x] if there is enough avaiable cash
# #       [x] Buy using all available cash
# #[x] If sell action
# #   [x] get referenced coin dollar amount
# #   [x] sell all referenced coin
# #[x] Use the correct cash amount for purchases
# #[x] Make trades only when time is not between 16:00 - 16:45
# #[ ] Cyber security spike. Find a way to protect long term investments. Use a different broker for day trades. Use a different account for day trades.
# #[ ] Make deployment pre/post action for fixing robin_stocks library
# #[ ] Figure out how to log in AWS lambda appropiately
# #[ ] Set buy order to expire immediately
# #[ ] Set sell order to expire immediately
# #[ ] Set text notification for buys and sell


# def robin_hood_trade(CONFIG, JSON):
#     # Login
#     robin_hood_login(CONFIG.RobinHood)

#     # Strip ticker to basic format
#     JSON['ticker'] = JSON['ticker'].replace('USD','')
    
#     # Get available investing funds
#     available_funds = get_available_cash_amount()
#     print(available_funds)
#     if is_trade_window():
#         if JSON['action'].lower() == 'buy':
#             if available_funds > 1: 
#                 return "BUY"
#                 #return buy_crypto(symbol=JSON['ticker'], dollar_amount=available_funds, price=float(JSON['price']))
#             else:
#                raise( Exception("No available funds for trading") )
#         if JSON['action'].lower() == 'sell':
#             # Get total current crypto dollar amount for referenced coin
#             crypto_dollar_amount = get_crypto_usd_value(JSON['ticker'])
#             return "SELL"
#             #return sell_crypto(symbol=JSON['ticker'], dollar_amount=crypto_dollar_amount, price=float(JSON['price']))

# # Sample Usage
# buy_JSON  = {"price": "14000.0" , "time": "2020-11-26T02:44:00Z", "ticker": "BTCUSD", "action": "buy" }
# sell_JSON = {"price": "20000.0" , "time": "2020-11-26T02:44:00Z", "ticker": "BTCUSD", "action": "sell" }

# print( robin_hood_trade(CONFIG, buy_JSON) )
# print( robin_hood_trade(CONFIG, sell_JSON) )

print( robin_hood_login(CONFIG.RobinHood) )
