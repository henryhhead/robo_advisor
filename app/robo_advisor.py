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

latest_close = parsed_response["Time Series (Daily)"]["2020-02-19"]["4. close"]



#
#INFO OUTPUTS
#



print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")