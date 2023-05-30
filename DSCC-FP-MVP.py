import yfinance as yf
import pandas as pd

# Define the ticker symbol for Apple
app_tickerSymbol = 'AAPL'

# Define the ticker symbol for Samsung
sam_tickerSymbol = '005930.KS'

# Define the start and end dates of the stocks
start_date = '2021-01-01'
end_date = '2021-12-31'

# Get the data for the stocks
apple_stock_data = yf.download(app_tickerSymbol, start=start_date, end=end_date)
samsung_stock_data = yf.download(sam_tickerSymbol, start=start_date, end=end_date)

# Store the data in a pandas dataframe
df_apple = pd.DataFrame(apple_stock_data)
df_samsung = pd.DataFrame(samsung_stock_data)

print(df_apple)
print(df_samsung)