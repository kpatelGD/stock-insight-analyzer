# Stock Insight Analyzer

An educational Python tool that takes a stock ticker (e.g., `AAPL`, `TSLA`, `MSFT`), downloads one year of market data from Yahoo Finance, calculates a set of well-known technical indicators, visualizes the price trend, and produces a simple rule-based recommendation: *long-term investing*, *short-term trading*, or *use caution*.

> ⚠️ This project is **educational only**. It is not financial advice and should not be used to make real investment decisions.

---

## Features

- Fetches 1 year of historical stock data via the `yfinance` API.
- Calculates key indicators:
  - Current price, 52-week high / low
  - Average daily volume
  - 20-day and 50-day simple moving averages
  - Annualized volatility
  - 1-month and 6-month returns
  - 14-day Relative Strength Index (RSI)
- Generates a **rule-based recommendation** with an explainable score, risk rating, and reasons.
- Saves a labeled price-trend chart with moving averages (PNG).
- Saves a plain-text report summarizing metrics and reasoning.
- Handles invalid tickers, empty input, and network errors gracefully.

---

## Project Structure

```
stock-insight-analyzer/
├── main.py                   # entry point
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── fetch_data.py         # downloads data from Yahoo Finance
│   ├── indicators.py         # moving averages, RSI, summary metrics
│   ├── analyzer.py           # rule-based recommendation logic
│   ├── visualizer.py         # matplotlib price chart
│   └── utils.py              # formatting, printing, report saving
├── reports/
│   └── charts/               # saved chart images
└── data/
    └── sample_outputs/       # saved text reports
```

---

## Setup

### 1. Clone or download the project

```bash
git clone https://github.com/<your-username>/stock-insight-analyzer.git
cd stock-insight-analyzer
```

### 2. (Optional but recommended) Create a virtual environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run

From the project root directory:

```bash
python main.py
```

You will be prompted for a stock ticker. Example session:

```
==================================================
         STOCK INSIGHT ANALYZER
   Educational tool - not financial advice
==================================================

Enter a stock ticker (e.g., AAPL, TSLA, MSFT): AAPL

===== STOCK INSIGHT ANALYZER =====
Ticker: AAPL
Company: Apple Inc.
Sector: Technology
Industry: Consumer Electronics
Current Price: $189.45
52-Week Range: $164.08 - $199.62
Average Volume: 58,241,500
20-Day Moving Average: $187.62
50-Day Moving Average: $182.11
Annualized Volatility: 22.14%
1-Month Return: 1.45%
6-Month Return: 12.80%
RSI (14): 57.22

===== RECOMMENDATION =====
Recommendation: Better suited for long-term investing
Signal Score: 8
Risk Score (1-10): 3
Summary: This stock shows a relatively healthy trend with supportive
momentum and manageable risk levels based on the indicators used in this project.
Reasons:
- Current price is above the 50-day moving average.
- 20-day moving average is above the 50-day moving average, showing positive short-term momentum.
- Six-month performance is strong.
- Volatility is relatively moderate.
- RSI is in a balanced range.

Chart saved to:  reports/charts/AAPL_trend.png
Report saved to: data/sample_outputs/AAPL_report.txt
```

---

## How the Recommendation Works

The program is **rule-based** (not machine learning) so that every recommendation can be explained. Each indicator contributes points to a signal score:

| Rule                                                  | Points |
| ----------------------------------------------------- | ------ |
| Current price above 50-day MA                         | +2 / -2 |
| 20-day MA above 50-day MA (positive short-term trend) | +2 / -1 |
| Strong 6-month return (> 10%)                         | +2     |
| Positive 6-month return (0% – 10%)                    | +1     |
| Negative 6-month return                               | -2     |
| Moderate volatility (< 25% annualized)                | +2     |
| High volatility (> 40% annualized)                    | -2     |
| RSI in balanced range (30 – 70)                       | +1     |
| RSI overbought (> 70)                                 | -1     |

Final label:

- **Score ≥ 5** → *Better suited for long-term investing*
- **Score 2 – 4** → *May be suitable for short-term trading*
- **Score < 2** → *Use caution*

The risk score (1–10) is derived from volatility and the final label.

---

## Architecture (Input → Processing → Output)

```
           +-------------------+
 USER ---> |  main.py (CLI)    |
           +---------+---------+
                     |
                     v
           +-------------------+          +------------------------+
           | src/fetch_data.py | <----->  | Yahoo Finance (yfinance)|
           +---------+---------+          +------------------------+
                     |
                     v
           +-------------------+
           | src/indicators.py |  (MA20, MA50, RSI, volatility, returns)
           +---------+---------+
                     |
                     v
           +-------------------+
           | src/analyzer.py   |  (rule-based scoring)
           +---------+---------+
                     |
            +--------+--------+
            v                 v
  +-------------------+  +-----------------------+
  | src/visualizer.py |  |  src/utils.py         |
  | (PNG chart)       |  |  (console + .txt)     |
  +-------------------+  +-----------------------+
```

---

## Testing Checklist

- [x] Valid ticker (e.g., `AAPL`, `MSFT`, `TSLA`) produces metrics and chart
- [x] Invalid ticker shows a friendly error message
- [x] Empty input shows a friendly error message
- [x] Network errors are handled gracefully
- [x] Chart displays without crashing
- [x] Moving averages, RSI, and volatility calculations are correct
- [x] Recommendation is produced with reasons
- [x] Report file is written to `data/sample_outputs/`

---

## Requirements

- Python 3.10+
- pandas
- numpy
- matplotlib
- yfinance

Install with `pip install -r requirements.txt`.

---

## License / Disclaimer

This project was developed as part of a Python class assignment. It is intended for educational purposes only and does not constitute financial advice.
