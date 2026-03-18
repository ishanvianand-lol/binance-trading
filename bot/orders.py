from bot.client import FuturesClient
from bot.validators import * 
from bot.logging_config import setLogger

logger = setLogger()
client = FuturesClient()

def placeOrder(symbol, side, type, qty, price=None, stopPrice=None):
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
        logger.info(f"Response: {response}")
        return response
    
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise