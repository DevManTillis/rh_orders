import pyotp 
import robin_stocks as r
import datetime
from pytz import timezone
import inspect
from jsonschema import validate


def validate_input(JSON: dict) -> bool:
    try:
        print("Validating Serverless Event Input")
        schema = {
             "type" : "object",
             "properties": {
                 "ticker" : {"type" : "string"},
                 "price" : {"type" : "number"},
                 "order_type" : {"type" : "string"},
                 "alert_type" : {"type" : "string"}
             },
        }
        validate(instance=JSON, schema=schema)
        print("Validation OK")
        return True
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False


def robin_hood_authcode(CONFIG: object) -> str:
    try:
        print("Log into robinhood API")
        two_factor_auth_code = pyotp.TOTP(CONFIG.authcode).now()
        return two_factor_auth_code
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False


def robin_hood_login(CONFIG: object) -> str:
    try:
        print("Log into robinhood API")
        two_factor_auth_code = pyotp.TOTP(CONFIG.authcode).now()
        r.login(CONFIG.user, CONFIG.password, mfa_code=two_factor_auth_code, store_session=False)
        return two_factor_auth_code
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False


def get_order_quit_time(date_time_str: str) -> object:
    try:
        quit_time = (datetime.datetime.fromisoformat(date_time_str.replace('Z', '+00:00')) + datetime.timedelta(hours=8))
        return quit_time
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False


def get_available_cash_amount() -> float:
    try:
        print("Get available trade funds/cash")
        return float(r.account.load_phoenix_account()['account_buying_power']['amount'])
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False


def is_trade_window() -> bool:
    # trading view does not provide proper data between 16:00 - 16:45
    # so trades only begin after or before this window
    try:
        print("Check if trade window is open")
        now = datetime.datetime.now()
        now = timezone('US/Pacific').localize(now)
        trade_window_end = datetime.datetime.fromisoformat(str(datetime.date.today()) + "T16:00:00+00:00")
        trade_window_start = datetime.datetime.fromisoformat(str(datetime.date.today()) + "T16:45:00+00:00")
        if (now > trade_window_end) and (now < trade_window_start):
            print("Trade window is closed. No trade completed.")
            return False
        else:
            print("Trade Window is open")
            return True
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False


def sell_crypto_limit(symbol: str, dollar_amount: float, price: float) -> bool:
    try:
        print(f"Limit Order Sell of all {symbol} coin")
        dollar_amount = get_crypto_usd_value(ticker=symbol)
        quantity = round( (dollar_amount / price), 8 )
        r.order_sell_crypto_limit(symbol=symbol, quantity=quantity, price=price, timeInForce='gtc')
        return True
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False


def sell_crypto_market(symbol: str) -> bool:
    try:
        r.order_sell_crypto_by_quantity(symbol=symbol, quantity=get_crypto_quantity(ticker=symbol), timeInForce='gtc')
        return True
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False


def get_crypto_usd_value(ticker: str) -> float:
    try:
        ticker = ticker.upper()
        currencies = [ currency for currency in r.get_crypto_positions() if 'currency' in currency.keys() ]
        coin = [ coin for coin in currencies if str(coin['currency']['code']).upper() == ticker ][0]
        return float( coin['cost_bases'][0]['direct_cost_basis'] )
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False


def get_crypto_quantity(ticker: str) -> float:
    try:
        ticker = ticker.upper()
        currencies = [ currency for currency in r.get_crypto_positions() if 'currency' in currency.keys() ]
        coin = [ coin for coin in currencies if str(coin['currency']['code']).upper() == ticker ][0]
        quantity = coin['quantity']
        return float(quantity)
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False


def get_currency_id(symbol: str) -> str:
    try:
        for item in r.get_crypto_currency_pairs():
            if item['asset_currency']['code'] == symbol:
                return item['id']
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False


def get_crypto_orders() -> list:
    try:
        return r.orders.get_all_open_crypto_orders()
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False


def cancel_crypto_orders(symbol: str) -> bool:
    try:
        for order in get_crypto_orders():
            if order['currency_pair_id'] == get_currency_id(symbol=symbol):
                r.cancel_crypto_order(order['id'])
        return True
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False      


def get_current_price(symbol: str) -> float:
    try:
        return float(r.get_crypto_quote(symbol=symbol)['bid_price'])
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False


# def subscriber_push(JSON: dict, parent_id: str) -> bool:
#     """
#     Send JSON payload to all other subscribers to this parent service
#     """
#     try:
#         JSON['parent_id'] = parent_id
#         return True
#     except Exception as e:
#         print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
#         return False


def stock_stop_loss_order(symbol: str, trigger_sell_price: float) -> bool:
    try:
        print(f"Stop Loss Order Sell of all {symbol} coin")
        # cancel_crypto_orders(symbol=symbol)
        # sell_crypto_market(symbol=symbol)
        return True
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False


def stop_loss_order(symbol: str, trigger_sell_price: float) -> bool:
    try:
        print(f"Stop Loss Order Sell of all {symbol} coin")
        cancel_crypto_orders(symbol=symbol)
        sell_crypto_market(symbol=symbol)
        return True
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False


def take_profit_order(symbol: str, trigger_sell_price: float) -> bool:
    try:
        print(f"Stop Loss Order Sell of all {symbol} coin")
        cancel_crypto_orders(symbol=symbol)
        sell_crypto_market(symbol=symbol)
        return True
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))
        return False
