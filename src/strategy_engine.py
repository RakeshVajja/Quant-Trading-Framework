import pandas as pd


class StrategyEngine:

    def __init__(self, strategy_name="ema_crossover"):
        self.strategy_name = strategy_name

    def generate_signals(self, df):
        if self.strategy_name == "ema_crossover":
            return self._ema_crossover(df)
        else:
            raise ValueError("Unsupported strategy")

    def _ema_crossover(self, df):
        df = df.copy()

        df["EMA10"] = df["Close"].ewm(span=10, adjust=False).mean()
        df["EMA30"] = df["Close"].ewm(span=30, adjust=False).mean()
        df["EMA200"] = df["Close"].ewm(span=200, adjust=False).mean()
        close = df["Close"]
        if isinstance(close, pd.DataFrame):
            close = close.iloc[:, 0]

        # regime
        df["regime"] = 0
        df.loc[close > df["EMA200"], "regime"] = 1
        df.loc[close < df["EMA200"], "regime"] = -1

        df["signal"] = 0
        # Long crossover
        df.loc[(df["EMA10"] > df["EMA30"]) & (df["EMA10"].shift(1) <= df["EMA30"].shift(1)) & (df["regime"] == 1), "signal"] = 1
        # Short crossover
        df.loc[(df["EMA10"] < df["EMA30"]) & (df["EMA10"].shift(1) >= df["EMA30"].shift(1)) & (df["regime"] == -1), "signal"] = -1

        df["position"] = df["signal"].replace(0, method = "ffill").fillna(0)
        print(df["position"].value_counts())
        return df

