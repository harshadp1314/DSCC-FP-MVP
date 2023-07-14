from prophet import Prophet
import pandas as pd
import yfinance as yf

df_apple = yf.download('aapl', '2021-01-01', '2021-12-31')
df_samsung = yf.download('005930.KS', '2021-01-01', '2021-12-31')

df_apple.reset_index(inplace=True)
df_samsung.reset_index(inplace=True)
df_apple['Date'] = pd.to_datetime(df_apple['Date'])
df_samsung['Date'] = pd.to_datetime(df_samsung['Date'])

df_apple = df_apple[['Date', 'Close']].copy()
df_samsung = df_samsung[['Date', 'Close']].copy()

df_apple_1 = df_apple.rename(columns = {'Date' : 'ds', 'Close' : 'y'})
# df_apple_1.head()

df_samsung_1 = df_samsung.rename(columns = {'Date' : 'ds', 'Close' : 'y'})
# df_samsung_1.head()

def price_forecasting(df, period):
    
    m = Prophet()
    m.fit(df)
    future_price = m.make_future_dataframe(periods=period)
    forecast = m.predict(future_price)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    
    # plot the foreasts
    fig = m.plot(forecast)
    
    # plot the components 
    fig2 = m.plot_components(forecast)
    
    return fig, fig2

price_forecasting(df_apple_1, 365)

price_forecasting(df_samsung_1, 365)

