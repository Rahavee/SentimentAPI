from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from newsapi import NewsApiClient
import datetime

def getnews(term):
    today = datetime.date.today()
    daysAgo = datetime.timedelta(days=3)
    dateDaysAgo = today - daysAgo
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


def sentiment():
    data = getnews()
    analyzer = SentimentIntensityAnalyzer()
    for sentence in data:
        if sentence["content"] is not None:
            vs = analyzer.polarity_scores(sentence["content"])
            sentence["polarity"] = vs
    return data




