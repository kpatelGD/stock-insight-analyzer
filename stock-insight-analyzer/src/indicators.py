from __future__ import annotations

import math
import pandas as pd


TRADING_DAYS = 252


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Add common indicators used in the project."""
    data = df.copy()
    data["Daily Return"] = data["Close"].pct_change()
    data["MA20"] = data["Close"].rolling(window=20).mean()
    data["MA50"] = data["Close"].rolling(window=50).mean()
    data["RSI14"] = compute_rsi(data["Close"], period=14)
    return data


def compute_rsi(series: pd.Series, period: int = 14) -> pd.Series:
    """Compute RSI using average gains and losses."""
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss.replace(0, pd.NA)
    rsi = 100 - (100 / (1 + rs))
    return rsi.fillna(50)


def calculate_summary_metrics(df: pd.DataFrame) -> dict:
    """Create a summary metrics dictionary for analysis and output."""
    latest = df.iloc[-1]
    close_series = df["Close"]
    daily_returns = df["Daily Return"].dropna()

    current_price = float(latest["Close"])
    high_52 = float(close_series.max())
    low_52 = float(close_series.min())
    avg_volume = float(df["Volume"].mean()) if "Volume" in df.columns else 0.0
    ma20 = float(latest["MA20"]) if not math.isnan(latest["MA20"]) else current_price
    ma50 = float(latest["MA50"]) if not math.isnan(latest["MA50"]) else current_price
    volatility = float(daily_returns.std() * math.sqrt(TRADING_DAYS)) if not daily_returns.empty else 0.0

    if len(close_series) >= 126:
        six_month_return = float((current_price / close_series.iloc[-126]) - 1)
    else:
        six_month_return = float((current_price / close_series.iloc[0]) - 1)

    if len(close_series) >= 21:
        one_month_return = float((current_price / close_series.iloc[-21]) - 1)
    else:
        one_month_return = float((current_price / close_series.iloc[0]) - 1)

    price_vs_ma50_pct = float((current_price - ma50) / ma50) if ma50 else 0.0
    rsi = float(latest["RSI14"]) if "RSI14" in df.columns else 50.0

    return {
        "current_price": current_price,
        "high_52_week": high_52,
        "low_52_week": low_52,
        "average_volume": avg_volume,
        "ma20": ma20,
        "ma50": ma50,
        "annualized_volatility": volatility,
        "six_month_return": six_month_return,
        "one_month_return": one_month_return,
        "price_vs_ma50_pct": price_vs_ma50_pct,
        "rsi14": rsi,
    }