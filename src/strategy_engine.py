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

        df["EMA20"] = df["Close"].ewm(span=20).mean()
        df["EMA50"] = df["Close"].ewm(span=50).mean()

        df["signal"] = 0
        df.loc[df["EMA20"] > df["EMA50"], "signal"] = 1
        df.loc[df["EMA20"] < df["EMA50"], "signal"] = -1

        return df

