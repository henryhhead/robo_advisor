# app/robo_advisor.py

# get_data.py
import csv
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)
 

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="OOPS")

symbol = "TSLA"

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

print("REQUESTING SOME DATA FROM THE INTERNET...")
response = requests.get(request_url)

#handle response error

if "Error Message" in response.text:
    print("OOps couldn't find that symbol, please try again.")
    exit()


parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys()) #TODO: Assumes first day is on top, but consider sorting to ensure latest day is first


latest_day = dates[0]
latest_close = tsd[latest_day]["4. close"] # TODO: sort to ensure latest day is first

high_prices = []
low_prices = []

for date in dates:
    high_price = (tsd[date]["2. high"])
    high_prices.append(float(high_price))
    low_price = (tsd[date]["3. low"])
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

buy = "Buy"
reason = "The latest closing price is more than 20 percent above its recent close."

if float(latest_close) < 1.2 * float(recent_low):
    buy = "Don't Buy"
    reason = "The latest closing price is less than 20 percent above its recent close."

#
#INFO OUTPUTS
#

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")


print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print(f"RECOMMENDATION: {buy}!")
print(f"RECOMMENDATION REASON: {reason}")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")



csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        daily_prices = tsd[date]
        prices = {
              
        }
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"], 
            "high": daily_prices["2. high"], 
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"], 
            "volume": daily_prices["5. volume"]

            })

      