import pandas_datareader
import re
import datetime

result = pandas_datareader.nasdaq_trader.get_nasdaq_symbols(retry_count=3, timeout=30, pause=None)

print(len(result))


def autoComplete(search):
    match = []

    for i in range(0, len(result)):
        if re.search(str(search), result.iloc[i, 9]) is not None:
            print(result.iloc[i, 9])
            match.append({"Name": result.iloc[i, 1], "Symbol": result.iloc[i, 9]})
        if len(match) == 11:
            break

    return match


def getStockData(stock):
    data = pandas_datareader.DataReader(stock, data_source="yahoo", start="2013-01-01", end=datetime.date.today())
    closingPrice=[]
    for i in range(0, len(data)):
        closingPrice.append(float(data.iloc[i,3]))
    return closingPrice

