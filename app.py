from fastapi import FastAPI, HTTPException
import yfinance as yf
from typing import Optional
from datetime import datetime

app = FastAPI(title="Stock Data API", version="1.0")

@app.get("/")
def home():
    return {"message": "Welcome to the Stock Data API. Use /stock/{ticker} to get stock data."}

@app.get("/stock/{ticker}")
def get_stock_info(ticker: str):
    """
    Fetches basic stock information.
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        return {
            "ticker": ticker.upper(),
            "company_name": info.get("longName", "N/A"),
            "sector": info.get("sector", "N/A"),
            "industry": info.get("industry", "N/A"),
            "current_price": info.get("currentPrice", "N/A"),
            "open_price": info.get("open", "N/A"),
            "day_high": info.get("dayHigh", "N/A"),
            "day_low": info.get("dayLow", "N/A"),
            "market_cap": info.get("marketCap", "N/A"),
            "volume": info.get("volume", "N/A"),
            "employees": info.get("fullTimeEmployees", "N/A"),
            "currency": info.get("currency", "N/A"),
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stock/{ticker}/history")
def get_stock_history(ticker: str, start: Optional[str] = None, end: Optional[str] = None, period: Optional[str] = "1mo"):
    """
    Fetches historical stock data.
    - If `start` and `end` dates are provided, it fetches data for that range.
    - If not, it fetches data for the last month (`1mo`) by default.
    """
    try:
        stock = yf.Ticker(ticker)
        if start and end:
            df = stock.history(start=start, end=end)
        else:
            df = stock.history(period=period)

        if df.empty:
            raise HTTPException(status_code=404, detail="No historical data found")

        return {
            "ticker": ticker.upper(),
            "history": df.reset_index().to_dict(orient="records")
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stock/{ticker}/dividends")
def get_stock_dividends(ticker: str):
    """
    Fetches stock dividend history.
    """
    try:
        stock = yf.Ticker(ticker)
        dividends = stock.dividends.reset_index().to_dict(orient="records")

        if not dividends:
            raise HTTPException(status_code=404, detail="No dividend data available")

        return {
            "ticker": ticker.upper(),
            "dividends": dividends
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stock/{ticker}/splits")
def get_stock_splits(ticker: str):
    """
    Fetches stock split history.
    """
    try:
        stock = yf.Ticker(ticker)
        splits = stock.splits.reset_index().to_dict(orient="records")

        if not splits:
            raise HTTPException(status_code=404, detail="No stock split data available")

        return {
            "ticker": ticker.upper(),
            "splits": splits
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

