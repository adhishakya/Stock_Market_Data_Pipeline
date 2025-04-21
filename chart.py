import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh
import plotly.express as px
from db_connection import get_db_connection

st_autorefresh(interval=5000, key='auto-refresh')

conn = get_db_connection()

def get_stock_data():
    query = '''
        SELECT * FROM stock_prices ORDER BY trade_timestamp DESC;
    '''
    return pd.read_sql(query, conn)

st.title('Real-Time Stock Dashboard')

df = get_stock_data()

symbols = df['symbol'].unique().tolist()
if 'selected_symbols' not in st.session_state:
    st.session_state.selected_symbols = symbols

selected_symbols = st.multiselect(
    'Select Stocks to View',
    options=symbols,
    default=st.session_state.selected_symbols,
    key='stock_selector'
)

st.session_state.selected_symbols = selected_symbols

filtered_df = df[df['symbol'].isin(selected_symbols)]

st.subheader('Raw Data')
st.dataframe(filtered_df)

for symbol in selected_symbols:
    st.subheader(f'{symbol} - Price Over Time')
    symbol_df = filtered_df[filtered_df['symbol'] == symbol].copy()
    symbol_df['trade_timestamp'] = pd.to_datetime(symbol_df['trade_timestamp'], unit='ms')
    symbol_df = symbol_df.sort_values('trade_timestamp')

    fig = px.line(
        symbol_df,
        x = 'trade_timestamp',
        y = 'last_price',
        title = f'{symbol} Stock Price Over Time',
        labels = {'trade_timestamp': 'Time', 'last_price': 'Price'}
    )
    fig.update_layout(
        xaxis_title = 'Time',
        yaxis_title = 'Price',
        xaxis_rangeslider_visible = False,
        template = 'plotly_dark'
    )
    st.plotly_chart(fig, use_container_width=True)
