from DSCC_FP_MVP import fetch_stock_data
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing, ExponentialSmoothing
from pmdarima.arima import auto_arima
from statsmodels.tsa.arima.model import ARIMA
import seaborn as sns
import numpy as np

df = fetch_stock_data('aapl')
df['Date'] = pd.to_datetime(df['Date'])

def moving_averages():
    ma = df[['Date', 'Open']].copy()
    ma.set_index('Date', inplace=True)
    # ma.index = pd.to_datetime(df.index)
    ma = ma.resample('1M').mean()

    ma['M3'] = ma['Open'].rolling(window=3).mean()
    # Plot the moving averages
    fig, ax = plt.subplots(figsize=(15, 6))
    ma.plot(ax=ax)

    # Set x-axis limits
    left = ma.index.min()
    right = ma.index.max()
    # ax.set_xlim(left - pd.DateOffset(days=360), right + pd.DateOffset(days=360))

    # Display the plot
    plt.show()

def exponential_smoothing():
    span = 3

    alpha = 2/(span+1)

    df['ES3'] = SimpleExpSmoothing(ma['Open']).fit(smoothing_level= alpha, optimized=False).fittedvalues.shift(-1)
    df[['Open', 'ES3']].plot(figsize=(15,6))
    # plt.show()

    df = df.reindex(index=df.index[::])

    df_train, df_val = df[:int(len(df)*0.95)], df[int(len(df)*0.95):]

    df_val = df_val.set_index('Date', drop=False)
    df_train = df_train.set_index('Date', drop=True)

    fig, ax = plt.subplots(figsize=(15, 6))
    # sns.lineplot(data=df_train, x=df_train.index, y='Open', color='black', ax=ax)
    # sns.lineplot(data=df, x='Date', y='Open')

    ax.set_title('Open Price', fontsize = 20, loc='center', fontdict=dict(weight='bold'))
    ax.set_xlabel('Year', fontsize=16, fontdict=dict(weight='bold'))
    ax.set_ylabel('Price', fontsize=16, fontdict=dict(weight='bold'))
    plt.tick_params(axis='y', which='major', labelsize=16)
    plt.tick_params(axis='x', which='major', labelsize=6)
    plt.legend(loc='upper right', labels = ('train', 'test'))
    plt.show()

def model():

    # model_autoARIMA = auto_arima(df_train['Open'])

    # print(model_autoARIMA)

    model = ARIMA(df['Close'], order = (1, 1, 1))

    fitted = model.fit()
    forecast = fitted.forecast(steps=30)  # Change the number of steps as needed

    forecast_values = np.array(forecast)

    # Plot the actual and forecasted prices
    plt.plot(df['Date'], df['Close'], label='Actual Price')
    plt.plot(df['Date'].iloc[-1:] + pd.DateOffset(days=1), forecast_values, label='Forecasted Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Apple Stock Price Forecast with ARIMA')
    plt.legend()
    plt.show()