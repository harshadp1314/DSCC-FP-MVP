import streamlit as st
import pandas as pd
from DSCC_FP_MVP_Storage import retrieve_data_from_s3
import plotly.graph_objs as pplt
from DSCC_FP_MVP_Visualization import candle_stick_graph

st.write("""
Stock Data Dashboard
""")

st.sidebar.header('User Input')

def get_input():
    start_date = st.sidebar.text_input("Start Date", "2020-01-01")
    end_date = st.sidebar.text_input("End Date", "2020-12-31")
    stock_symbol = st.selectbox("Stock Symbol", ("Apple", "Samsung"))
    chart_type = st.selectbox("Select Chart Type", ("Line Pattern", "Candle Stick Pattern"))

    return start_date, end_date, stock_symbol, chart_type

def get_data(symbol, start, end):
    if symbol == 'Apple':
        df = retrieve_data_from_s3('apple_stock')
    elif symbol == 'Samsung':
        df = retrieve_data_from_s3('samsung_stock')
    else:
        df = pd.DataFrame(columns=['Date', 'Open', 'Close', 'High', 'Low', 'Volume'])

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    start_row = 0
    end_row = 0

    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = 1
            break

    for j in range(0, len(df)):
        if end <= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df)-1-j
            break
    
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row+1, :]

start, end, symbol, chart_type = get_input()

df = get_data(symbol, start, end)

if chart_type == "Line Pattern":
    st.header(symbol+" Close Price\n")
    st.line_chart(df['Close'])

    st.header(symbol+ "Volume\n")
    st.line_chart(df['Volume'])

    st.header(symbol+" Open Price\n")
    st.line_chart(df['Open'])

    st.header("Stock Data")
    st.write(df)

    st.header("Data Statistics")
    st.write(df.describe())
elif chart_type == "Candle Stick Pattern":
    fig = candle_stick_graph(df)
    st.plotly_chart(fig)