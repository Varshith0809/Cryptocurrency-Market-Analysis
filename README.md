# 🪙 Cryptocurrency Market Analysis Dashboard

An interactive dashboard built with **Streamlit** that analyzes cryptocurrency market data using the public **CoinGecko API**.
It provides real-time price snapshots, historical charts, risk metrics, and correlations for selected cryptocurrencies.

---

## ✨ Features

* 📊 **Market Snapshot** – Current price, market cap, volume, % changes (24h/7d/30d)
* 📈 **Historical Price Charts** – Line charts for selected coins (30–365 days)
* 🔄 **Daily Returns & Cumulative Returns**
* ⚡ **Risk Metrics** – Rolling volatility, max drawdown, Sharpe-like ratio
* 🔗 **Correlation Matrix** – Compare returns between assets
* 🖥 **Interactive UI** – Select coins and time horizon from the sidebar
* 📥 **Downloadable CSVs** (optional extension)

---

## 🚀 Installation & Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/crypto-market-analysis.git
cd crypto-market-analysis
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt**

```txt
streamlit
pandas
numpy
matplotlib
requests
```

### 3. Run the app

```bash
streamlit run streamlit_app.py
```

Then open 👉 [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🖥 Usage

* Select coins (BTC, ETH, SOL, BNB, XRP, etc.) from the **sidebar**
* Choose historical lookback (30–365 days)
* Click **Run Analysis** to generate tables, charts, and risk metrics

---

## 📂 Project Structure

```
crypto-market-analysis/
│── streamlit_app.py     # Main Streamlit dashboard
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
│── crypto_market_outputs/ (optional for CSVs)
```

---

## 📸 Screenshots

### Market Snapshot

*(example table)*

| Asset | Price (USD) | Market Cap | 24h % |  7d % | 30d % |
| ----- | ----------: | ---------: | ----: | ----: | ----: |
| BTC   |     113,500 |       2.2T | +2.1% | +8.4% |  +16% |

### Charts

* Price history (line chart)
* Rolling volatility (30D)
* Drawdowns

---

## 🌐 Deployment

### Option 1: Localhost (for personal use)

Follow the steps above.

### Option 2: Deploy on [Streamlit Cloud](https://streamlit.io/cloud)

1. Push this repo to GitHub
2. Log in to Streamlit Cloud
3. Click **New App → Connect Repo → Select Branch → Deploy**
4. You’ll get a public URL 🎉

---

## 📜 License

This project is licensed under the MIT License – see [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

* [CoinGecko API](https://www.coingecko.com/en/api) for free cryptocurrency data
* [Streamlit](https://streamlit.io) for the interactive dashboard framework

---


