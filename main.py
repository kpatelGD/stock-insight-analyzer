from src.fetch_data import get_stock_history, get_stock_info
from src.indicators import add_indicators, calculate_summary_metrics
from src.analyzer import generate_recommendation
from src.visualizer import plot_price_trend
from src.utils import normalize_ticker, print_summary, print_recommendation, ensure_output_dirs


def main() -> None:
    ensure_output_dirs()

    raw_ticker = input("Enter stock ticker (e.g., AAPL): ").strip()
    ticker = normalize_ticker(raw_ticker)

    if not ticker:
        print("Error: ticker cannot be empty.")
        return

    try:
        history = get_stock_history(ticker, period="1y")
        info = get_stock_info(ticker)
        history = add_indicators(history)
        metrics = calculate_summary_metrics(history)
        recommendation = generate_recommendation(metrics)

        print_summary(ticker, info, metrics)
        print_recommendation(recommendation)

        chart_path = plot_price_trend(history, ticker)
        print(f"\nChart saved to: {chart_path}")

    except ValueError as exc:
        print(f"Error: {exc}")
    except Exception as exc:
        print(f"Unexpected error: {exc}")


if __name__ == "__main__":
    main()