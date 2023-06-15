#!/usr/bin/env python
# coding: utf-8

# ### Importing Required Libraries

# In[1]:


from DSCC_FP_MVP_StatisticalAnalysis import calculate_statistics
from DSCC_FP_MVP_Visualization import visualize_data

#!pip install yfinance
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


# ### Defining Class and Functions for Extracting Modules from Analysis and Visualization Files

# In[2]:


class StockDataAnalyzer:
    
    def __init__(self, symbol):
        self.symbol = symbol
    
    def fetch_stock_data(self):
        """
        Fetches the stock data using the yfinance API.
        """
        stock_data = yf.download(self.symbol, start=start_date, end=end_date)
        return stock_data

    def analyze_data(self, symbol):
        """
        Performs analysis on the fetched stock data.
        """
        stock_data = self.fetch_stock_data()
        statistics_data = calculate_statistics(stock_data)
        visualize_data(stock_data, symbol)
        return statistics_data
    
    def df_stock_data(self, symbol):
        """
        Performs analysis on the fetched stock data.
        """
        stock_data = self.fetch_stock_data()
        return stock_data
    


# ### Defining Parameters for Fetching the Data

# In[3]:


# Define the ticker symbol for Apple and Samsung
symbol_apple = 'AAPL'
symbol_samsung = '005930.KS'

# Define the start and end dates
start_date = '2021-01-01'
end_date = '2021-12-31'


# ### Calling Functions and Displaying Statistics

# In[4]:


apple_analyzer = StockDataAnalyzer(symbol_apple)
df_apple = pd.DataFrame(apple_analyzer.df_stock_data(symbol_apple))
df_apple.reset_index(inplace=True)

df_apple.describe()


# In[5]:


samsung_analyzer = StockDataAnalyzer(symbol_samsung)
df_samsung = pd.DataFrame(samsung_analyzer.df_stock_data(symbol_samsung))
df_samsung.reset_index(inplace=True)

df_samsung.describe()


# ### Displaying Dimensions and Checking for Null Values

# In[8]:


df_apple.shape


# In[9]:


df_samsung.shape


# In[10]:


df_apple.isna().sum()


# In[11]:


df_samsung.isna().sum()


# ### Displaying the Visualization Graphs

# In[ ]:


apple_statistics = apple_analyzer.analyze_data(symbol_apple)
print(f"Apple Stock Statistics: {apple_statistics}")


# In[ ]:


samsung_statistics = samsung_analyzer.analyze_data(symbol_samsung)
print(f"Samsung Stock Statistics: {samsung_statistics}")


# ### Displaying Final Statistics

# In[ ]:


# Create a pandas DataFrame to display the statistics
df = pd.DataFrame([apple_statistics, samsung_statistics], index=["Apple", "Samsung"])

# Display the DataFrame
df.head()


# In[ ]:




