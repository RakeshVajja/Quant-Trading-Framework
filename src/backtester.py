import pandas as pd

class Backtester:

    def __init__(self,initial_capital=100000):
        self.initial_capital = initial_capital

    def run(self, df):
        df = df.copy()
        df["returns"] = df["Close"].pct_change()
        df["stratergy_returns"] = df["returns"] * df["signal"].shift(1)

        df["equity_curve"] = (1 + df["stratergy_returns"]).cumprod() * self.initial_capital

        return df
