from data_engine import DataEngine
from strategy_engine import StrategyEngine

data_engine = DataEngine()
df = data_engine.fetch_data("PNB.NS", period="1y", interval="1d")

strategy = StrategyEngine(strategy_name="ema_crossover")
df = strategy.generate_signals(df)

print(df[["Close", "EMA20", "EMA50", "signal"]].tail())
