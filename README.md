# TechQuake  
### Analyzing the Behavior of Major Tech Stocks During Market Shocks (2018–2024)

This project examines how major technology companies responded to recent market stress events — including the **COVID-19 crash** and the **2022 inflation-driven selloff**.  
Using historical daily price data, the analysis compares:

- **AAPL** — Apple  
- **MSFT** — Microsoft  
- **NVDA** — Nvidia  
- **AMZN** — Amazon  
- **SPOT** — Spotify  

It focuses on three core dimensions of stock behavior:

1. **Cumulative performance** (long-term growth)  
2. **Rolling volatility** (short-term risk)  
3. **Drawdowns** (declines from previous peaks)

The goal is to understand whether large tech companies behave similarly during market shocks,  
and how high-growth vs. established firms differ in risk and resilience.

---

## Project Structure

```
techquake/
│
├── stock_data/
│   ├── fetch_data.py         
│   ├── process_data.py        
│   └── visualizations.py      
├── presentation/
│   └── techquake.ipynb        
├── requirements.txt           
└── README.md                  

```
---

## Methodology

### **1. Data Collection**
Historical price data is downloaded from Yahoo Finance using `yfinance`.  
The project uses daily **OHLCV** data (Open/High/Low/Close/Volume),  
but analysis focuses on **closing prices**.

### **2. Data Processing**
The following transformations are applied:

- Clean and extract price tables  
- Compute **daily returns**  
- Build **cumulative return indices** (indexed to 100)  
- Compute **21-day rolling volatility**  
- Compute **drawdowns** (decline from running peaks)

### **3. Visualization**
Custom plotting functions highlight:

- How stock performance diverges over time  
- How volatility spikes during crises  
- How deeply each stock fell during stress periods  

Major events highlighted in the analysis include:

- **2020-03-16 — COVID-19 crash**  
- **2022-06-13 — Inflation-driven market selloff**

---

## Key Findings

### **1. Performance Divergence**
- NVDA shows explosive long-term growth but also deeper downturns.  
- AAPL and MSFT show slow, steady compounding — the most resilient performers.  
- SPOT displays the weakest long-term trend with large fluctuations.

### **2. Volatility Behavior**
- All stocks show sharp volatility spikes during COVID-19 and mid-2022.  
- NVDA and AMZN experience the largest jumps in volatility.  
- AAPL and MSFT remain relatively stable even under stress.  
- SPOT shows sustained high volatility due to a younger, less diversified business model.

### **3. Drawdown Analysis**
- **SPOT** had the deepest maximum drawdown (~80%).  
- **NVDA** experienced large drawdowns but recovered faster.  
- **AAPL** and **MSFT** had the smallest, shortest drawdowns — the “safe havens” of tech.  
- **AMZN** lies in between: significant declines but less extreme than SPOT.

---

## Why This Analysis Matters

This project helps illustrate how different categories of tech companies behave during crises:

- **Investors** can identify which tech stocks maintain stability under pressure.  
- **Analysts** can compare risk profiles between high-growth and megacap firms.  
- **Students** can learn key financial concepts: returns, volatility, drawdowns, and market shocks.  
- **Researchers** can build upon the modular code for further quantitative analysis.

---

## How to Run the Project

Clone the repository:

```bash
git clone https://github.com/arevikosipyan/techquake.git
cd techquake

Install Dependencies: 

pip install -r requirements.txt

Open the notebook:

jupyter notebook presentation/techquake.ipynb

License

This project is licensed under the MIT License.