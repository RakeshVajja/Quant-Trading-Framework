def calculate_cagr(df, initial_capital):
    final_value = df["equity_curve"].iloc[-1]
    years = len(df) / 252
    cagr = (final_value / initial_capital) ** (1 / years) - 1
    return cagr

def calculate_sharpe_ratio(df, risk_free_rate=0):
    daily_returns = df["stratergy_returns"].dropna()
    excess_returns = daily_returns - (risk_free_rate / 252)
    sharpe = (excess_returns.mean() / excess_returns.std()) * (252 ** 0.5)
    return sharpe

def calculate_max_drawdown(df):
    equity = df["equity_curve"]
    rolling_max = equity.cummax()
    drawdown = (equity / rolling_max) - 1
    return drawdown.min()


