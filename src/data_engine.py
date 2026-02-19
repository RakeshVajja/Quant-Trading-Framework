import yfinance as yf
import pandas as pd

class DataEngine:
    def __init__(self, provider="yfinance"):
        self.provider = provider

    def fetch_data(self, ticker, period="1y", interval="1d"):
        if self.provider == "yfinance":
            return self._fetch_yfinance(ticker, period, interval)
        else:
            raise ValueError("Unsupported data provider")

    def _fetch_yfinance(self, ticker, period, interval):
        df = yf.download(ticker, period=period, interval=interval)

        if df.empty:
            raise ValueError("No data returned. Check ticker symbol.")

        df = df.dropna()
        df = df.sort_index()

        return df

