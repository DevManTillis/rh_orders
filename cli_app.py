#!/usr/bin/env python3
# from RobinHood import buy_crypto, sell_crypto, robin_hood_login, get_available_cash_amount, get_crypto_usd_value, is_trade_window
import inspect
from chalicelib.config import CONFIG
from chalicelib.RobinHood import robin_hood_login
import robin_stocks as r

print( robin_hood_login(CONFIG.RobinHood) )

def stock_stop_loss_order(symbol: str) -> bool:
    try:
        stock_orders = r.find_stock_orders(symbol=symbol)
        instruments = list()

        # Check all orders, cancel pending order for queued ticker
        for order in stock_orders:
            if order['state'] == "queued":
                instruments.append(order['instrument'])
                r.cancel_stock_order(order['id'])
                print(f"Order for {symbol} canceled.")

        open_positions = r.get_open_stock_positions()
        print(instruments)
        print(open_positions.keys())
        for position in open_positions:
            if position['instrument'] in instruments:
                # print(r.order_sell_market(symbol=symbol, quantity=position['quantity'], timeInForce="gtc", extendedHours=False))
                print(r.order_sell_fractional_by_price(symbol=symbol, amountInDollars=position, timeInForce="gtc", extendedHours=False))
                print(f"Market sell order submitted for {symbol}.")
            else:
                print(f"No current orders matching {symbol}. No market order submission.")

        return True
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False

stock_stop_loss_order(symbol="SI")

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


