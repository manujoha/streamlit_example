import streamlit as st
import pandas as pd
import yfinance as yf


# Define function to retrieve stock data from Yahoo Finance API
def get_stock_data(symbol):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period='max')
    return data


# Define Streamlit app
def app():
    st.title('Alphabet (Google) Stock Prices')
    st.write('This app displays daily stock prices for Alphabet (Google).')

    # Retrieve and display stock data
    symbol = 'GOOGL'
    data = get_stock_data(symbol)
    st.write('**Symbol:**', symbol)
    st.write('**Last Close:**', data['Close'].iloc[-1])
    st.write('**Last Volume:**', data['Volume'].iloc[-1])
    st.write('**Price Chart:**')
    st.line_chart(data['Close'])


if __name__ == '__main__':
    app()