import yfinance as yf
import matplotlib.pyplot as plt

# Get user input
ticker = input("Enter stock ticker (e.g., AAPL): ")

# Fetch stock data
stock = yf.Ticker(ticker)
data = stock.history(period="1y")

# Check if data exists
if data.empty:
    print("Invalid ticker or no data found.")
    exit()

# Print first few rows
print("\nStock Data Preview:")
print(data.head())

# Plot closing price
plt.figure(figsize=(10, 5))
plt.plot(data['Close'], label='Closing Price')

plt.title(f"{ticker} Stock Price (1 Year)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()

plt.show()