from __future__ import annotations

from pathlib import Path


def normalize_ticker(ticker: str) -> str:
    return ticker.strip().upper()


def format_currency(value: float | int | None) -> str:
    if value is None:
        return "N/A"
    return f"${value:,.2f}"


def format_large_number(value: float | int | None) -> str:
    if value is None:
        return "N/A"
    return f"{value:,.0f}"


def format_percent(value: float | int | None) -> str:
    if value is None:
        return "N/A"
    return f"{value * 100:.2f}%"


def print_summary(ticker: str, info: dict, metrics: dict) -> None:
    print("\n===== STOCK INSIGHT ANALYZER =====")
    print(f"Ticker: {ticker}")
    print(f"Company: {info.get('company_name', ticker)}")
    print(f"Sector: {info.get('sector', 'N/A')}")
    print(f"Industry: {info.get('industry', 'N/A')}")
    print(f"Current Price: {format_currency(metrics['current_price'])}")
    print(
        f"52-Week Range: {format_currency(metrics['low_52_week'])} - {format_currency(metrics['high_52_week'])}"
    )
    print(f"Average Volume: {format_large_number(metrics['average_volume'])}")
    print(f"20-Day Moving Average: {format_currency(metrics['ma20'])}")
    print(f"50-Day Moving Average: {format_currency(metrics['ma50'])}")
    print(f"Annualized Volatility: {format_percent(metrics['annualized_volatility'])}")
    print(f"1-Month Return: {format_percent(metrics['one_month_return'])}")
    print(f"6-Month Return: {format_percent(metrics['six_month_return'])}")
    print(f"RSI (14): {metrics['rsi14']:.2f}")


def print_recommendation(recommendation: dict) -> None:
    print("\n===== RECOMMENDATION =====")
    print(f"Recommendation: {recommendation['label']}")
    print(f"Signal Score: {recommendation['score']}")
    print(f"Risk Score (1-10): {recommendation['risk_score']}")
    print(f"Summary: {recommendation['summary']}")
    print("Reasons:")
    for reason in recommendation["reasons"]:
        print(f"- {reason}")


def ensure_output_dirs() -> None:
    Path("reports/charts").mkdir(parents=True, exist_ok=True)
    Path("data/sample_outputs").mkdir(parents=True, exist_ok=True)