from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from newsapi import NewsApiClient
import datetime


def getnews(term):
    today = datetime.date.today()
    daysAgo = datetime.timedelta(days=3)
    dateDaysAgo = today - daysAgo
    try:
        newsapi = NewsApiClient(api_key='64e56e0c1c8944469ca51458fea97e73')
        all_articles = newsapi.get_everything(q=term,
                                              from_param=dateDaysAgo,
                                              to=today,
                                              language='en',
                                              sort_by='relevancy',
                                              page=1)

        data = []
        for article in all_articles["articles"]:
            data.append({"content": article["content"], "title": article["title"], "url": article["url"]})
        return data
    except Exception:
        return "Nothing"


def sentiment(term):
    try:
        data = getnews(term)
        analyzer = SentimentIntensityAnalyzer()
        for sentence in data:
            if sentence["content"] is not None:
                vs = analyzer.polarity_scores(sentence["content"])
                sentence["polarity"] = vs
                print(type(vs))
        return data
    except Exception:
        return "Nothing"


print(sentiment("NCLH"))
