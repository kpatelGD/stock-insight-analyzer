from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


OUTPUT_DIR = Path("reports/charts")


def plot_price_trend(df: pd.DataFrame, ticker: str) -> str:
    """Create and save a stock price chart with moving averages."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / f"{ticker.upper()}_trend.png"

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df.index, df["Close"], label="Close Price", color="#1f77b4", linewidth=1.6)
    ax.plot(df.index, df["MA20"], label="20-Day MA", color="#ff7f0e", linewidth=1.4)
    ax.plot(df.index, df["MA50"], label="50-Day MA", color="#2ca02c", linewidth=1.4)

    # Mark the most recent close so the chart has a focal point
    last_date = df.index[-1]
    last_close = df["Close"].iloc[-1]
    ax.scatter([last_date], [last_close], color="#d62728", zorder=5)
    ax.annotate(
        f"  ${last_close:,.2f}",
        xy=(last_date, last_close),
        color="#d62728",
        fontsize=10,
        fontweight="bold",
    )

    ax.set_title(f"{ticker.upper()} Stock Trend (1 Year)", fontsize=14, fontweight="bold")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend(loc="upper left")

    fig.tight_layout()
    fig.savefig(output_path, dpi=120)
    plt.close(fig)

    return str(output_path)
