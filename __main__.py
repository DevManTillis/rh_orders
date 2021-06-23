from app import robin_hood_trade
import inspect
from chalicelib.config import CONFIG


if __name__ == '__main__':
    try:
        JSON = {"ticker": "ETHUSD", "price": 2007.53, "time": "2021-03-13T22", "order_type": "stop_loss"}
        robin_hood_trade(CONFIG=CONFIG, JSON=JSON)
    except Exception as e:
        print(f"ERROR: {__name__}.{inspect.stack()[0][3]}: " + str(e))