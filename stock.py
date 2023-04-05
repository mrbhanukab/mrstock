import requests
from bs4 import BeautifulSoup
import asyncio
import telegram


async def send_message(ticker, company_name, latest_update, closing_price, previous_close, intradaychange):
    bot = telegram.Bot(token="5970479672:AAH17INZd_4NvnrIj221zZzUSwk7kOxpp6M")
    chat_id = "Your Chat Id (For More Information Read ReadMe.md)"
    message = f"<b><u>{company_name} | {ticker}</u></b>\n\n<i>⌛ {latest_update}</i>\n\n<b>Closing Price:</b> {closing_price}\n<b>Previous Close:</b> {previous_close}\n<b>Intra-Day Change:</b> {intradaychange}\n"
    message += "\n<b><a href='https://www.marketwatch.com/investing/stock/{}/charts?countrycode=lk&mod=mw_quote_advanced'>View Advance Chart 📊</a></b>".format(ticker)
    await bot.send_message(chat_id=chat_id, text=message, parse_mode="HTML")

def get_data(ticker):
    url = f"https://www.marketwatch.com/investing/stock/{ticker}?countrycode=lk"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    company_name_el = soup.select_one("h1.company__name")
    company_name = company_name_el.text.strip()

    latest_update_el = soup.select_one("span.timestamp__time")
    latest_update = latest_update_el.text.strip()

    closing_price_el = soup.select_one("h2.intraday__price span.value")
    closing_price = closing_price_el.text.strip()

    previous_close_el = soup.select_one("td.u-semi")
    previous_close = previous_close_el.text.strip()

    intraday_change_el = soup.select_one("bg-quote.intraday__change")
    if intraday_change_el is not None:
        change_percent_el = intraday_change_el.select_one("span.change--percent--q")
        change_percent = change_percent_el.text.strip()
        if "positive" in intraday_change_el["class"]:
            intradaychange = f"📈 {change_percent}"
        else:
            intradaychange = f"📉 {change_percent}"
    else:
        intradaychange = "N/A"

    return company_name, latest_update, closing_price, previous_close, intradaychange

async def main():
    tickers = ["odel.n0000", "ahpl.n0000"]
    tasks = []
    for ticker in tickers:
        data = get_data(ticker)
        company_name, latest_update, closing_price, previous_close, intradaychange = data
        task = asyncio.create_task(send_message(ticker, company_name, latest_update, closing_price, previous_close, intradaychange))
        tasks.append(task)

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
