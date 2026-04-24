from __future__ import annotations

import yfinance as yf
import pandas as pd


def get_stock_history(ticker: str, period: str = "1y") -> pd.DataFrame:
    """Fetch historical stock data for a ticker.

    Raises:
        ValueError: if the ticker is invalid, no data is returned,
                    or the connection to Yahoo Finance fails.
    """
    try:
        stock = yf.Ticker(ticker)
        history = stock.history(period=period, auto_adjust=False)
    except Exception as exc:
        # Network errors, SSL errors, yfinance internal errors, etc.
        raise ValueError(
            f"Could not download data for '{ticker}'. "
            f"Check your internet connection and that the ticker is correct. "
            f"(Details: {exc})"
        )

    if history is None or history.empty:
        raise ValueError(
            f"No data returned for '{ticker}'. "
            f"The ticker may be invalid or delisted."
        )

    history = history.copy()
    history.dropna(subset=["Close"], inplace=True)

    if history.empty:
        raise ValueError("No usable closing price data was returned.")

    return history


def get_stock_info(ticker: str) -> dict:
    """Fetch company metadata for a ticker.

    Always returns a dictionary with sensible defaults. Failures in
    yfinance's .info call are swallowed so they do not crash the demo.
    """
    defaults = {
        "company_name": ticker.upper(),
        "market_cap": None,
        "currency": "USD",
        "sector": "N/A",
        "industry": "N/A",
    }

    try:
        stock = yf.Ticker(ticker)
        info = getattr(stock, "info", None) or {}
    except Exception:
        # yfinance's .info is notoriously flaky. Don't let it kill the run.
        return defaults

    return {
        "company_name": info.get("longName") or info.get("shortName") or ticker.upper(),
        "market_cap": info.get("marketCap"),
        "currency": info.get("currency") or "USD",
        "sector": info.get("sector") or "N/A",
        "industry": info.get("industry") or "N/A",
    }
