import pandas_datareader
import re
import datetime

file = open("./stock.txt", "r")
result = []
for i in range(0, 17996):
    result.append(re.search(".*", file.readline()).group())

file.close()



def autoComplete(search):
    match = []
    for i in range(1, len(result),2):
        if re.search(str(search), result[i]) is not None:
            match.append({"Name": result[i-1], "Symbol": result[i]})
        if len(match) == 11:
            break

    return match


def getStockData(stock):
    data = pandas_datareader.DataReader(stock, data_source="yahoo", start="2017-01-01", end=datetime.date.today())
    closingPrice = []
    for i in range(0, len(data)):
        closingPrice.append({"date":data.iloc[i,0], "price" :float(data.iloc[i, 3])})
    return closingPrice

