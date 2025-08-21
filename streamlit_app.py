# streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
import requests, time, os
import matplotlib.pyplot as plt

st.set_page_config(page_title="Crypto Market Analysis", layout="wide")

VS_CURRENCY = "usd"

def fetch_markets(coin_ids):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": VS_CURRENCY,
        "ids": ",".join(coin_ids),
        "order": "market_cap_desc",
        "per_page": len(coin_ids),
        "page": 1,
        "sparkline": False,
        "price_change_percentage": "24h,7d,30d"
    }
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    return pd.DataFrame(r.json())

def fetch_price_history(coin_id, days=365):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": VS_CURRENCY, "days": days}
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    data = r.json()
    prices = data.get("prices", [])
    df = pd.DataFrame(prices, columns=["ts", coin_id])
    df["date"] = pd.to_datetime(df["ts"], unit="ms")
    return df.set_index("date").drop(columns=["ts"])

def compute_drawdown(series):
    cummax = series.cummax()
    return series / cummax - 1.0

def sharpe_like(returns, periods_per_year=365):
    mu = returns.mean() * periods_per_year
    sigma = returns.std() * np.sqrt(periods_per_year)
    return np.where(sigma == 0, np.nan, mu / sigma)

# ---------------- UI ----------------
st.title("📊 Cryptocurrency Market Analysis")

coins = st.sidebar.multiselect(
    "Select coins:", 
    ["bitcoin","ethereum","solana","binancecoin","ripple","cardano","dogecoin"],
    default=["bitcoin","ethereum","solana"]
)
days = st.sidebar.slider("Days of history:", 30, 365, 180)

if st.sidebar.button("Run Analysis"):
    # Snapshot
    snapshot = fetch_markets(coins)
    st.subheader("Market Snapshot")
    st.dataframe(snapshot[["id","symbol","current_price","market_cap","total_volume"]])

    # Prices
    st.subheader("Price History")
    price_data = []
    for coin in coins:
        df = fetch_price_history(coin, days)
        price_data.append(df)
        time.sleep(1.2)
    prices = pd.concat(price_data, axis=1)
    st.line_chart(prices)

    # Returns & Risk
    returns = prices.pct_change().dropna()
    cum_returns = (1+returns).cumprod()-1
    vol = returns.rolling(30).std()*np.sqrt(365)
    drawdowns = prices.apply(compute_drawdown)

    risk_table = pd.DataFrame({
        "Sharpe_like": sharpe_like(returns),
        "Vol_30d_ann": vol.tail(1).T.squeeze(),
        "Max_Drawdown": drawdowns.min()
    })
    st.subheader("Risk Metrics")
    st.dataframe(risk_table)

    # Charts
    st.subheader("Rolling 30D Volatility")
    st.line_chart(vol)

    st.subheader("Drawdowns")
    st.line_chart(drawdowns)

    # Correlations
    st.subheader("Return Correlation")
    st.dataframe(returns.corr())
