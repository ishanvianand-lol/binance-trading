def validateSide(side):
    if side not in ["BUY", "SELL"]: 
        raise ValueError("Side can only be buy/sell")
    
def validateType(type):
    if type not in ["MARKET","LIMIT", "STOP"]:
        raise ValueError("Order type can only be market/limit/stop")
    
def validateQty(qty):
    if qty <= 0:
        raise ValueError("Quantity should be more than 0")
    

def validatePrice(type, price):
    if type=="LIMIT" and price is None:
        raise ValueError("Price is a must for limit orders")
    
def validateStop(type, price, stopPrice):
    if type=="STOP":
        if price is None:
            raise ValueError('Stop requires price')
        if stopPrice is None:
            raise ValueError('Stop requires stop price')