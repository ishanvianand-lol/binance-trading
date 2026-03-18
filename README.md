## Setup

1. Create virtual environment
2. Install dependencies:
   pip install -r requirements.txt

3. Add .env:
   BINANCE_API_KEY=xxx
   BINANCE_API_SECRET=yyy

## Run

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.002

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.002 --price 70000

## Notes

- Uses Binance Futures Testnet
