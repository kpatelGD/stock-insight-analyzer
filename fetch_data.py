from __future__ import annotations

import yfinance as yf
import pandas as pd


def get_stock_history(ticker: str, period: str = "1y") -> pd.DataFrame:
    """Fetch historical stock data for a ticker."""
    stock = yf.Ticker(ticker)
    history = stock.history(period=period, auto_adjust=False)

    if history.empty:
        raise ValueError("Invalid ticker or no data returned.")

    history = history.copy()
    history.dropna(subset=["Close"], inplace=True)

    if history.empty:
        raise ValueError("No usable closing price data was returned.")

    return history


def get_stock_info(ticker: str) -> dict:
    """Fetch company metadata for a ticker."""
    stock = yf.Ticker(ticker)
    info = getattr(stock, "info", None) or {}

    return {
        "company_name": info.get("longName") or info.get("shortName") or ticker.upper(),
        "market_cap": info.get("marketCap"),
        "currency": info.get("currency") or "USD",
        "sector": info.get("sector") or "N/A",
        "industry": info.get("industry") or "N/A",
    }
