import logging
from binance.um_futures import UMFutures

# ========== Setup Logging ==========
logging.basicConfig(
    filename="futures_tradebot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ========== Initialize Client ==========
def init_client(api_key, api_secret, base_url):
    try:
        client = UMFutures(key=api_key, secret=api_secret, base_url=base_url)
        logging.info("Client initialized successfully.")
        return client
    except Exception as e:
        logging.error(f"Client initialization failed: {e}")
        raise

# ========== Get Account Info ==========
def show_account_info(client):
    try:
        account = client.account()
        print("Account Info:\n", account)
        logging.info("Fetched account info.")
    except Exception as e:
        print("Failed to fetch account info:", e)
        logging.error(f"Error fetching account info: {e}")

# ========== Get Market Price ==========
def get_price(client, symbol):
    try:
        data = client.ticker_price(symbol=symbol)
        price = float(data["price"])
        print(f"Current {symbol} price: {price}")
        return price
    except Exception as e:
        logging.error(f"Price fetch error: {e}")
        raise

# ========== Place Order ==========
def place_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):
    try:
        params = {
            "symbol": symbol,
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": float(quantity)
        }
        if order_type.upper() == "LIMIT":
            if price is None:
                raise ValueError("Price required for LIMIT orders.")
            params["price"] = str(price)
            params["timeInForce"] = "GTC"
        elif order_type.upper() in ["STOP", "TAKE_PROFIT"]:
            if stop_price is None or price is None:
                raise ValueError("Both stop price and limit price are required for STOP/TAKE_PROFIT orders.")
            params["stopPrice"] = str(stop_price)
            params["price"] = str(price)
            params["timeInForce"] = "GTC"

        order = client.new_order(**params)
        print("✅ Order placed successfully:", order)
        logging.info(f"Order placed: {order}")
        return order
    except Exception as e:
        print("❌ Order placement failed:", e)
        logging.error(f"Order error: {e}")
        return None

# ========== Get Balance ==========
def get_balance(client):
    try:
        balances = client.balance()
        usdt_balance = next((item for item in balances if item['asset'] == 'USDT'), None)
        if usdt_balance:
            print(f"USDT Balance: {usdt_balance['balance']}")
            logging.info(f"Fetched USDT balance: {usdt_balance['balance']}")
        else:
            print("USDT balance not found.")
    except Exception as e:
        print("Failed to fetch balance:", e)
        logging.error(f"Balance fetch error: {e}")

# ========== Main Script ==========
if __name__ == "__main__":
    API_KEY = "" # fill the creds here
    API_SECRET = "" # fill the creds here
    BASE_URL = "https://testnet.binancefuture.com"

    client = init_client(API_KEY, API_SECRET, BASE_URL)
    # show_account_info(client)

    while True:
        print("\nOrder Type: 1 - MARKET, 2 - LIMIT, 3 - BALANCE, 4 - EXIT, 5 - STOP-LIMIT")
        type_input = input("Enter your choice (1/2/3/4/5): ")
        order_type_map = {"1": "MARKET", "2": "LIMIT", "3": "BALANCE", "4": "EXIT", "5": "STOP"}
        order_type = order_type_map.get(type_input, "MARKET")

        if order_type == "BALANCE":
            get_balance(client)
            continue
        elif order_type == "EXIT":
            print("Exiting bot...")
            break

        symbol = input("Enter trading pair symbol (e.g., BTCUSDT): ")

        print("Order Side: 1 - BUY, 2 - SELL")
        side_input = input("Enter your choice (1/2): ")
        side = "BUY" if side_input == "1" else "SELL"

        quantity = float(input("Enter order quantity: "))
        price = None
        stop_price = None

        if order_type == "LIMIT":
            price = float(input("Enter limit price: "))
        elif order_type == "STOP":
            stop_price = float(input("Enter stop (trigger) price: "))
            price = float(input("Enter limit price after stop is triggered: "))

            print("STOP order will trigger a LIMIT order once stop price is hit.")

        try:
            get_price(client, symbol)
            place_order(client, symbol, side, order_type, quantity, price, stop_price)
        except Exception as e:
            print("Bot execution failed:", e)
