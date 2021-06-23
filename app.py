from chalice import Chalice
import inspect
from chalicelib.RobinHood import (
    sell_crypto_limit, 
    stop_loss_order,
    sell_crypto_market, 
    robin_hood_login, 
    get_available_cash_amount, 
    get_crypto_usd_value, 
    is_trade_window,
    validate_input,
    take_profit_order,
    stock_stop_loss_order
    )
from chalicelib.config import CONFIG, log
import sys


app = Chalice(app_name='tradingview-robinhood-stop-order-webhook-alert')

def robin_hood_trade(CONFIG, JSON):
    print("Start Transaction")

    if not validate_input(JSON=JSON):
        sys.exit("Input not validated. Use correct input.")

    if not robin_hood_login(CONFIG=CONFIG.RobinHood):
        sys.exit("Can't login. Check auth.")        

    # Strip ticker to basic format
    JSON['ticker'] = JSON['ticker'].replace('USD','')
        
    available_funds = get_available_cash_amount()
    
    if is_trade_window():
        if JSON['equity_type'] == "crypto":
            if JSON['order_type'].lower() == 'limit_sell_order':
                sell_crypto_limit(symbol=JSON['ticker'], price=float(JSON['price']))

            if JSON['order_type'].lower() == 'stop_loss':
                total_crypto_dollar_amount = get_crypto_usd_value(ticker=JSON['ticker'])
                stop_loss_order(symbol=JSON['ticker'], trigger_sell_price=JSON['price'])

            if JSON['order_type'].lower() == 'take_profit':
                total_crypto_dollar_amount = get_crypto_usd_value(ticker=JSON['ticker'])
                take_profit_order(symbol=JSON['ticker'], trigger_sell_price=JSON['price'])

        if JSON['equity_type'] == "stock":
            if JSON['order_type'].lower() == 'stop_loss':
                total_crypto_dollar_amount = get_crypto_usd_value(ticker=JSON['ticker'])
                stock_stop_loss_order(symbol=JSON['ticker'], trigger_sell_price=JSON['price'])

    print("End Transaction")
    return "SUCCESS"


@app.route('/', methods=['POST'])
def index():
    try:
        request = app.current_request
        webhook_message = request.json_body
        return {
                "result": True,
                "message": f"request initiated",
                "trade_result": robin_hood_trade(CONFIG, JSON=webhook_message)
                }
    except Exception as e:
        return {
                "result": False,
                "message": str(e)
                }