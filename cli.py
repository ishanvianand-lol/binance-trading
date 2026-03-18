import argparse
from bot.orders import placeOrder

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stopPrice", type=float)


    args = parser.parse_args()

    try:
        print("\nOrder Summary:")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.qty}")
        print(f"Price: {args.price}")

        response = placeOrder(
            symbol=args.symbol,
            side=args.side,
            type=args.type,
            qty=args.qty,
            price=args.price,
            stopPrice=args.stopPrice
        )

        print("\nResponse:")
        print(f"Order ID: {response.get('orderId','N/A')}")
        print(f"Status: {response.get('status','N/A')}")
        print(f"Executed Quantity: {response.get('executedQty','0')}")
        print(f"Client Order ID: {response.get('clientOorderId','N/A')}")


        print('\nOrder placed successfully')

    except Exception as e:
        print(f"\nOrder Failed: {str(e)}")
        

if __name__ == "__main__":
    main()