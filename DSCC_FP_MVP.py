import yfinance as yf
import pandas as pd
from DSCC_FP_MVP_Storage import store_data_in_s3

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

# Store the data in AWS S3
store_data_in_s3(df_apple)
store_data_in_s3(df_samsung)




# from DSCC_FP_MVP_Storage import store_data_in_dynamodb

# class DataProcessor:
#     def __init__(self, data):
#         self.data = data

#     def process_data(self):
#         # Perform data processing
#         processed_data = self.data  # Placeholder for actual processing

#         # Store the processed data in DynamoDB
#         store_data_in_dynamodb(processed_data)

# # Example usage
# if __name__ == "__main__":
#     data = df_samsung
#     processor = DataProcessor(data)
#     processor.process_data()
