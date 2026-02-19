from data_engine import DataEngine
from strategy_engine import StrategyEngine
from backtester import Backtester

data_engine = DataEngine()
df = data_engine.fetch_data("PNB.NS", period="1y", interval="1d")

strategy = StrategyEngine(strategy_name="ema_crossover")
df = strategy.generate_signals(df)

backtester = Backtester(initial_capital=100000)
df = backtester.run(df)

print(df[["Close", "signal", "equity_curve"]].tail())
