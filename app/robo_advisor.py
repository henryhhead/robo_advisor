# app/robo_advisor.py

# get_data.py
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)
 

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="OOPS") #HSA9J53W34ACUO9E

symbol = "TSLA"

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
#print("URL:", request_url)

print("REQUESTING SOME DATA FROM THE INTERNET...")
response = requests.get(request_url)
#print(type(response))
#print(response.status_code)
#pprint(type(response.text)) 

#handle response error

if "Error Message" in response.text:
    print("OOps couldn't find that symbol, please try again.")
    exit()


parsed_response = json.loads(response.text)
#print(type(parsed_response)) #> dictr 

# print(parsed_response)

 


last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

#breakpoint()

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys()) #TODO: Assumes first day is on top, but consider sorting to ensure latest day is first

latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"] # TODO: sort to ensure latest day is first



#high_prices = [10, 20, 30, 5 ]
#maximum of all high prices
#recent_high = max(high_prices)

high_prices = []
low_prices = []

for date in dates:
    high_price = (tsd[date]["2. high"])
    high_prices.append(float(high_price))
    low_price = (tsd[date]["3. low"])
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

#
#INFO OUTPUTS
#



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
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")