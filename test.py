import yfinance as yf
import pandas as pd
# Create a Ticker object for Tesla and SpaceX
tesla = yf.Ticker("TSLA")
spacex = yf.Ticker("SPCE")
# Fetch historical data for a specific time range
tesla_history = tesla.history(period="2y")  # Adjust the period as needed
spacex_history = spacex.history(period="2y")  # Adjust the period as needed
df1 = pd.DataFrame(tesla_history)
pd.set_option('display.max_columns', None)
print(df1)
df2 = pd.DataFrame(spacex_history)
pd.set_option('display.max_columns', None)
print(df2)
#print(tesla_history)
#print(spacex_history)