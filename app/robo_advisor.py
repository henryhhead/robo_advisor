# app/robo_advisor.py

# get_data.py
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


print("REQUESTING SOME DATA FROM THE INTERNET...")

API_KEY = os.getenv("HSA9J53W34ACUO9E", default="OOPS") #HSA9J53W34ACUO9E

symbol = "TSLA"

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
print("URL:", request_url)

response = requests.get(request_url)
print(type(response))
print(dir(response))
print(response.status_code)
print(type(response.text))

#handle response error

if "Error Message" in response.text:
    print("OOps couldn't find that symbol, please try again.")
    exit


parsed_response = json.loads(response.text)
print(type(parsed_response)) #> dictr 
print(parsed_response)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

#breakpoint()


#
#INFO OUTPUTS
#



print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: {last_refreshed}")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")