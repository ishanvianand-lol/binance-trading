from bot.client import FuturesClient
from bot.validators import * 
from bot.logging_config import setLogger
import time

logger = setLogger()

def placeOrder(symbol, side, type, qty, price=None, stopPrice=None):
    client = FuturesClient()
    symbol = symbol.upper()
    side = side.upper()
    type = type.upper()
    try:
        validateSide(side)
        validateType(type)
        validateQty(qty)
        validatePrice(type, price)

        params = {
            "symbol": symbol,
            "side": side,
            "type": type,
            "quantity": qty
        }

        if type=="LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"
        
        if type=="STOP":
            params["price"] = price
            params["stopPrice"] = stopPrice
            params["timeInForce"] = "GTC"

        print("FINAL PARAMS:", params)
        logger.info(f"Sending order: {params}")
        response = client.placeOrder(**params)
        order_id = response.get('orderId')
        for _ in range(10):
            order = client.client.futures_get_order(symbol=symbol, orderId=order_id)
            if order.get('status') in ('FILLED', 'CANCELED', 'EXPIRED', 'REJECTED'):
                response = order
                break
            time.sleep(0.5)

        logger.info(f"Response: {response}")
        return response
    
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise