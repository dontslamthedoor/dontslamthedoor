import streamlit as st
import pandas as pd
import yfinance as yf

st.title('Streamlit app to view US stocks.')

st.divider()

symbol = st.text_input('Enter a stock symbol')
st.divider()

e = st.container()

with e:
    ticker = yf.download(symbol, start='2021-01-01', end='2024-04-01')
    price = ticker.Close
    st.line_chart(price)

