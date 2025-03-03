# **Stock Data API**
A simple REST API built with **FastAPI** and **yfinance** to fetch stock market data.

## **Features**
- Fetch **real-time stock information** (price, volume, market cap, sector, etc.).
- Retrieve **historical stock data** (date range or predefined periods).
- Get **dividends and stock split history**.

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stock-data-api.git
   cd stock-data-api
   ```
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn yfinance
   ```
3. Run the API:
   ```bash
   uvicorn main:app --reload
   ```

## **API Endpoints**
| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET** | `/stock/{ticker}` | Get stock info (price, market cap, etc.). |
| **GET** | `/stock/{ticker}/history?period=1mo` | Get stock history (default: last month). |
| **GET** | `/stock/{ticker}/history?start=YYYY-MM-DD&end=YYYY-MM-DD` | Get historical data for a date range. |
| **GET** | `/stock/{ticker}/dividends` | Fetch dividend history. |
| **GET** | `/stock/{ticker}/splits` | Get stock split history. |

## **Example Usage**
- Fetch Apple stock data:
  ```bash
  curl -X GET "http://127.0.0.1:8000/stock/AAPL"
  ```
- Get Tesla's last 3 months history:
  ```bash
  curl -X GET "http://127.0.0.1:8000/stock/TSLA/history?period=3mo"
  ```
- Retrieve Amazon dividend data:
  ```bash
  curl -X GET "http://127.0.0.1:8000/stock/AMZN/dividends"
  ```

## **License**
MIT License. Free to use and modify.
