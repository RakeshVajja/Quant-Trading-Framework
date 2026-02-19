from data_engine import DataEngine

data_engine = DataEngine()
data = data_engine.fetch_data("PNB.NS", period="1y", interval="1d")

print(data.head())

