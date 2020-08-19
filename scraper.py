from gevent import monkey as curious_george

curious_george.patch_all(thread=False, select=False)
import grequests
from bs4 import BeautifulSoup
import re




def asyncFunc(term):
    url = ["https://money.cnn.com/quote/profile/profile.html?symb={}".format(term),
           "https://money.cnn.com/quote/shareholders/shareholders.html?symb={}&subView=institutional".format(term)]
    rs = (grequests.get(u) for u in url)
    res = grequests.map(rs)
    soup = []
    for r in res:
        soup.append(BeautifulSoup(r.text, "html.parser"))
    return soup


def getPercentageShares(soup):
    shares = soup.select("#wsod_institutionalTextAndPie table:nth-of-type(1) td")
    percentageShares = []
    for i in range(0, 6, 2):
        percentageShares.append(
            {"name": shares[i].text, "percent": re.match("[0-9,.,a-z,A-Z]*", shares[i + 1].text).group()})

    return percentageShares


def getTopInvesters(soup):
    names = soup.select("#wsod_shareholders table:nth-of-type(2) td:nth-child(1) span")
    stake = soup.select("#wsod_shareholders table:nth-of-type(2) .wsod_aRight:nth-child(2) ")
    investors = []
    for i in range(0, 10):
        investors.append({"name": names[i]['title'], "stake": stake[i + 1].text})

    return investors


def getTopMutualFunds(soup):
    names = soup.select("#wsod_shareholders table:nth-of-type(3) td:nth-child(1) span")
    stake = soup.select("#wsod_shareholders table:nth-of-type(3) .wsod_aRight:nth-child(2) ")
    mutualFunds = []
    for i in range(0, 10):
        mutualFunds.append({"name": names[i]['title'], "stake": stake[i + 1].text})

    return mutualFunds


def info(soup):

    desc = soup.select("#wsod_companyDescription")
    return desc[0].text



