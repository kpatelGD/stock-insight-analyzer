"""
Stock Insight Analyzer
----------------------
Entry point. Asks the user for a stock ticker, fetches one year of
historical data from Yahoo Finance, calculates a set of indicators,
prints a human-readable summary and a rule-based recommendation,
and saves a price-trend chart plus a text report.
"""
from src.fetch_data import get_stock_history, get_stock_info
from src.indicators import add_indicators, calculate_summary_metrics
from src.analyzer import generate_recommendation
from src.visualizer import plot_price_trend
from src.utils import (
    normalize_ticker,
    print_summary,
    print_recommendation,
    ensure_output_dirs,
    save_text_report,
)


BANNER = r"""
==================================================
         STOCK INSIGHT ANALYZER
   Educational tool - not financial advice
==================================================
"""


def run_for_ticker(ticker: str) -> None:
    """Run the full pipeline for a single ticker."""
    history = get_stock_history(ticker, period="1y")
    info = get_stock_info(ticker)
    history = add_indicators(history)
    metrics = calculate_summary_metrics(history)
    recommendation = generate_recommendation(metrics)

    print_summary(ticker, info, metrics)
    print_recommendation(recommendation)

    chart_path = plot_price_trend(history, ticker)
    report_path = save_text_report(ticker, info, metrics, recommendation)

    print(f"\nChart saved to:  {chart_path}")
    print(f"Report saved to: {report_path}")


def main() -> None:
    ensure_output_dirs()
    print(BANNER)

    try:
        raw_ticker = input("Enter a stock ticker (e.g., AAPL, TSLA, MSFT): ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled by user.")
        return

    ticker = normalize_ticker(raw_ticker)
    if not ticker:
        print("Error: ticker cannot be empty. Please try again.")
        return

    try:
        run_for_ticker(ticker)
    except ValueError as exc:
        # Expected user-facing errors (bad ticker, no data, network)
        print(f"\nError: {exc}")
    except KeyboardInterrupt:
        print("\nCancelled by user.")
    except Exception as exc:
        # Anything we didn't anticipate - fail gracefully, do not crash
        print(f"\nUnexpected error: {exc}")
        print("Please try a different ticker or check your internet connection.")


if __name__ == "__main__":
    main()
