import logging
import os

def setLogger():
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/trading_bot.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger()