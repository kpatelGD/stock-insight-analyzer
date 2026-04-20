from __future__ import annotations

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


OUTPUT_DIR = Path("reports/charts")


def plot_price_trend(df: pd.DataFrame, ticker: str) -> str:
    """Create and save a stock price chart with moving averages."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / f"{ticker.upper()}_trend.png"

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Close"], label="Close Price")
    plt.plot(df.index, df["MA20"], label="20-Day MA")
    plt.plot(df.index, df["MA50"], label="50-Day MA")

    plt.title(f"{ticker.upper()} Stock Trend (1 Year)")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    return str(output_path)