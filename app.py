from flask import Flask
import fetchNews
import fetchTweets
import scraper
import stocks

app = Flask(__name__)


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
    soup = scraper.getWebpage(term)
    return {"status": "OK", "percentageShares": scraper.getPercentageShares(soup),
            "topInvestors": scraper.getTopInvesters(soup), "topMutualFunds": scraper.getTopMutualFunds(soup)}


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
    app.run(debug=True, port=80)
