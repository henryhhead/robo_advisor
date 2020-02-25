# robo_advisor

Run this code to help decide on buying a stock. To change the stock you are analyzing, change the four letter symbol listed under 'symbol'.


### Environment Setup


Create and activate a new Anaconda virtual environment:

conda create -n stocks-env python=3.7 # (first time only)

conda activate stocks-env


From within the virtual environment, install the required packages specified in the "requirements.txt" file you created:

pip install -r requirements.txt

From within the virtual environment, demonstrate your ability to run the Python script from the command-line:


python app/robo_advisor.py


Before using or devloping this application, take a moment to obtain an AlphaVantage API Key (https://www.alphavantage.co/support/#api-key) (e.g. "abc123)

After obtaining an API Key, create a new file in this repository called ".env" , and update the contents of the ".env" file to specify your real API Key:
 
    ALPHAVANTAGE_API_KEY="abc123"