import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class FuturesClient:
    def __init__(self):
        self.key = os.getenv("BINANCE_API_KEY")
        self.secret = os.getenv("BINANCE_API_SECRET")
        self.client = Client(self.key, self.secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
    
    def placeOrder(self, **params):
        return self.client.futures_create_order(**params)