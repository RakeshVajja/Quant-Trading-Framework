from data_engine import DataEngine
from strategy_engine import StrategyEngine
from backtester import Backtester
from metrics import calculate_cagr, calculate_sharpe_ratio, calculate_max_drawdown

data_engine = DataEngine()
df = data_engine.fetch_data("ICICIBANK.NS", period="5y", interval="1d")

strategy = StrategyEngine(strategy_name="ema_crossover")
df = strategy.generate_signals(df)

backtester = Backtester(initial_capital=100000)
df = backtester.run(df)
print("Total Trades:", df["position"].diff().abs().sum())
print("Time in Market:", round((df["position"] != 0).mean() * 100, 2), "%")

cagr = calculate_cagr(df, 100000)
sharpe = calculate_sharpe_ratio(df)
max_dd = calculate_max_drawdown(df)

print(df[["Close", "signal", "equity_curve"]].tail())

print("CAGR", round(cagr * 100, 2), "%")
print("Sharpe Ratio", round(sharpe, 2))
print("Max Drawdown", round(max_dd * 100, 2), "%")
