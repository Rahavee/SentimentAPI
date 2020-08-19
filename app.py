from gevent import monkey as curious_george
curious_george.patch_all(thread=False, select=False)
from flask import Flask
import fetchNews
import fetchTweets
import scraper
import stocks
import grequests
from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/news/<term>')
def news(term):
    return {"status": "OK", "content": fetchNews.sentiment(term)}


@app.route("/tweets/<term>")
def tweets(term):
    return {"status": "OK", "content": fetchTweets.run(term)}


@app.route("/data/<term>")
def data(term):
    soup = scraper.asyncFunc(term)
    return {"status": "OK", "percentageShares": scraper.getPercentageShares(soup[1]),
            "topInvestors": scraper.getTopInvesters(soup[1]), "topMutualFunds": scraper.getTopMutualFunds(soup[1]),"desc":scraper.info(soup[0])}


@app.route("/search/<term>")
def search(term):
    return {"status": "OK", "content": stocks.autoComplete(term)}


@app.route("/closingPrice/<stock>")
def closingPrice(stock):
    return {"status": "OK", "from": "2013-01-01", "stock": stock, "content": stocks.getStockData(stock)}


@app.route("/allData/<term>")

def allData(term):

    return {"news": news(term), "tweets": tweets(term), "scarper": data(term), "closing price": closingPrice(term)}

if __name__ == '__main__':
    app.run()
