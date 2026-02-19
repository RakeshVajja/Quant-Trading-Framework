import pandas as pd

class Backtester:

    def __init__(self,initial_capital=100000):
        self.initial_capital = initial_capital

    def run(self, df):
        df = df.copy()
        df["returns"] = df["Close"].pct_change()
        df["trade"] = df["position"].diff().abs()
        cost_per_trade = 0.001 #0.1% transaction cost
        df["stratergy_returns"] = (df["returns"] * df["position"].shift(1) - df["trade"] * cost_per_trade)
        
        df["equity_curve"] = (1 + df["stratergy_returns"]).cumprod() * self.initial_capital

        return df
