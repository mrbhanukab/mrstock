# Mr. Stock

This is a Python script that uses web scraping to fetch stock prices from [MarketWatch](https://www.marketwatch.com/) and sends the latest updates via Telegram.

## Requirements

- Python 3.7+
- `requests` module
- `beautifulsoup4` module
- `python-telegram-bot` module

## Installation

1. Clone this repository:

```
git clone https://github.com/mrbhanukab/mrstock.git
```

2. Install the required modules:

```
pip install -r requirements.txt
```

3. Create a new Telegram bot and obtain its API token. Refer to the [official Telegram Bot documentation](https://core.telegram.org/bots) for instructions.

4. Replace the `TOKEN` variable in the `main.py` file with your own Telegram bot API token.

5. Run the script:

```
python main.py
```

## How to get your Telegram chat ID

To get your Telegram chat ID, you can use the Telegram User Info Bot:

1. Add the Telegram User Info Bot (@userinfobot) to your Telegram contacts.
2. Start a chat with the bot and send any message.
3. The bot will reply with your chat ID, which you can use in the `chat_id` variable in the Python script.

Note that you should replace the `chat_id` variable in the `send_message()` function in the `main.py` script with your own chat ID obtained from the Telegram User Info Bot.


[![website](https://img.shields.io/badge/Github%20Page-mrbhanukab.github.io-lightgrey?style=for-the-badge&logo=GitHubr&logoColor=white)](https://mrbhanukab.github.io/)
<br>[![github](https://img.shields.io/badge/Github-mrbhanukab-%23333?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/mrbhanukab)<br>
[![twitter](https://img.shields.io/badge/Twitter-mrbhanuka-%2300acee?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/mrbhanuka)
