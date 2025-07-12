# Binance Futures Testnet Trading Bot

This is a simplified command-line trading bot that places market, limit, and stop-limit orders on the Binance **USDT-M Futures Testnet**. It also allows you to check your USDT balance.

---

## ✅ Features

* Place **Market**, **Limit**, and **Stop-Limit** orders
* Check **USDT Balance**
* Real-time price fetching
* Logging of all requests and responses
* Built using the official `binance-futures-connector` Python SDK

---

## 🧱 Prerequisites

* Python 3.8+
* Binance USDT-M Futures Testnet account
* API Key and Secret from the [Testnet Portal](https://testnet.binancefuture.com/)

---

## 🚀 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/BucBharat/binance-futures-bot.git
cd binance-futures-bot
```

2. **Install dependencies**

```bash
pip install binance-futures-connector
```

3. **Update your API credentials**
   In the script (`main.py`), replace:

```python
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
```

With your actual **Testnet** API Key and Secret.

---

## 💻 Running the Bot

```bash
python main.py
```

Follow the on-screen prompts to:

* Select order type
* Input trading symbol
* Choose BUY/SELL
* Set quantity and prices if applicable

---

## 📝 Logging

All API activity is logged to `futures_tradebot.log` for auditing and debugging.

---

## 📌 Notes

* This bot runs **only** on the Binance **Testnet** (not real funds).
* Ensure your API key has appropriate permissions (e.g., Futures Trading).
* Orders will fail if the symbol is incorrect or balance is insufficient.

---

## 🙋‍♂️ Support

For questions or issues, feel free to open an issue or contact via [GitHub Discussions](https://github.com/yourusername/binance-futures-bot/discussions).

Happy Trading! 🚀
