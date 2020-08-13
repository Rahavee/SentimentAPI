import pandas_datareader
result = pandas_datareader.nasdaq_trader.get_nasdaq_symbols(retry_count=3, timeout=30, pause=None)
print(type(result))
# stocks = []
#
# for i in range(len(result)):
#     stocks.append({"symbol":result["symbol"]})