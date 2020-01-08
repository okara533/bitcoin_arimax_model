import sys
import pandas as pd
from yahoofinancials import YahooFinancials


crypto_currencies=["BTC-USD","ETH-USD","LTC-USD"]
Yahoo_Api=YahooFinancials(crypto_currencies)
daily_prices=Yahoo_Api.get_historical_price_data("2013-01-01","2020-01-08","daily")
df=pd.DataFrame(daily_prices)

BTCUSD=pd.DataFrame(df["BTC-USD"]["prices"])
ETHUSD=pd.DataFrame(df["ETH-USD"]["prices"])
LTCUSD=pd.DataFrame(df["LTC-USD"]["prices"])

BTCUSD.to_csv("BTCUSD.csv")
ETHUSD.to_csv("ETHUSD.csv")
LTCUSD.to_csv("LTCUSD.csv")
