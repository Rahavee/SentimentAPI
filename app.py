from flask import Flask
import fetchNews
import fetchTweets
import scraper

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


@app.route("/data")
def data():
    return {"status": "OK", "percentageShares": scraper.getPercentageShares(),
            "topInvestors": scraper.getTopInvesters(), "topMutualFunds": scraper.getTopMutualFunds()}


if __name__ == '__main__':
    app.run()
