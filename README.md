# TechQuake  
### Behavior of Major Tech Stocks During Market Shocks

Are major tech stocks becoming more volatile as markets cycle through crises like COVID-19 and the 2022 inflation shock?  
Do high-growth names react differently to stress than established megacaps?

This project uses market data from **Yahoo Finance** to quantify how large technology companies behave during periods of turbulence.  
Rather than guessing which stocks are “safe” or “risky,” the analysis measures:

- **Cumulative performance** (long-term growth)  
- **Rolling volatility** (short-term instability)  
- **Drawdowns** (declines from previous peaks)

The goal is to examine whether tech companies — from Apple to Spotify — experience market shocks in similar or fundamentally different ways.

---

## 1. Data

All data comes from **Yahoo Finance** through the `yfinance` library.

### Tech stocks analyzed

The project focuses on five technology-related companies with different business models and risk profiles:

- **AAPL** — Apple  
- **MSFT** — Microsoft  
- **NVDA** — Nvidia  
- **AMZN** — Amazon  
- **SPOT** — Spotify  

These names span the spectrum from megacap “safe” tech (AAPL, MSFT) to high-growth semiconductors (NVDA) to consumer-facing platforms (AMZN, SPOT).

The dataset covers **daily prices from 2018–01–01 to present**.

---

## 2. Functionality

All core logic is implemented in the `stock_data` package.

### `stock_data.fetch_data`

- `fetch_stock_data(...)` – downloads OHLCV data from Yahoo Finance for selected tickers.

### `stock_data.process_data`

- `extract_price_table(...)` — isolate closing prices  
- `compute_daily_returns(...)` — compute day-over-day % returns  
- `compute_cumulative_returns(...)` — build cumulative index (base=100)  
- `compute_rolling_volatility(...)` — 21-day annualised volatility  
- `compute_drawdowns(...)` — running-maximum drawdowns

### `stock_data.visualizations`

Uses `matplotlib` for clean plotting:

- `plot_cumulative_returns(...)`  
- `plot_stock_comparison(...)`  
- `plot_volatility_with_events(...)`  

Events highlighted:

- **2020-03-16** — COVID-19 crash  
- **2022-06-13** — Inflation-driven tech selloff  

### Notebook

The full narrative analysis is in: presentation/techquake.ipynb

It performs the complete workflow:

1. Download data  
2. Clean prices and compute returns  
3. Calculate cumulative performance  
4. Compute and visualize rolling volatility  
5. Compute and analyze drawdowns  
6. Interpret results in context of market shocks  

---

## 3. Project Structure

```
techquake/
├── presentation/
│   └── techquake.ipynb 
├── stock_data/
│   ├── __init__.py
│   ├── fetch_data.py         
│   ├── process_data.py        
│   └── visualizations.py
├── app.py             
├── LICENSE
├── README.md   
└── requirements.txt                  

```
---

## 4. Installation

### Clone the repository

```bash
git clone https://github.com/arevikosipyan/techquake.git
cd techquake
```
Install dependencies:

```bash
pip install -r requirements.txt
```
Open the notebook:
```bash
jupyter notebook presentation/techquake.ipynb
```

## 5. Analysis

The notebook performs the full workflow:

- Downloads historical OHLCV data  
- Extracts and cleans closing prices  
- Computes returns and cumulative indices  
- Computes rolling volatility and drawdowns  
- Visualizes performance and risk under market stress  

Each figure includes an explanation of what the chart reveals.

---

## 6. Key Findings

### 1. Long-Term Performance
- NVDA shows the strongest growth but also the largest swings.  
- AAPL and MSFT show steady compounding with limited instability.  
- SPOT performs weakest, with high volatility and limited long-term growth.

### 2. Volatility Behavior
- All stocks show volatility spikes during March 2020 and mid-2022.  
- NVDA and AMZN exhibit the largest volatility jumps.  
- AAPL and MSFT remain the most stable.  
- SPOT stays elevated for prolonged periods.

### 3. Drawdowns
- SPOT experiences the deepest maximum drawdown (~80%).  
- NVDA shows deep declines but recovers quickly.  
- AAPL and MSFT have the smallest drawdowns.  
- AMZN sits in the middle with moderate but persistent declines.

---

## 7. Why This Analysis Matters

This project is useful for:

- **Investors** — assessing resilience of different tech stocks  
- **Students** — understanding volatility, returns, drawdowns, crisis behavior  
- **Analysts** — comparing risk between high-growth and megacap firms  
- **Researchers** — using the modular code for extended analysis  

It highlights that tech companies do **not** respond uniformly to market shocks.

---

## 8. Limitations

- Uses daily data from 2018 onward
- No valuation or fundamental metrics included
- Analysis is descriptive, not predictive
- This is not investment advice