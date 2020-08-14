import requests
from bs4 import BeautifulSoup
import re


def getWebpage(term):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    url = "https://money.cnn.com/quote/shareholders/shareholders.html?symb={}&subView=institutional".format(term)
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup


def getPercentageShares(soup):
    shares = soup.select("#wsod_institutionalTextAndPie table:nth-of-type(1) td")
    percentageShares = []
    for i in range(0,6,2):
        percentageShares.append({"name":shares[i].text,"percent":re.match("[0-9,.,a-z,A-Z]*", shares[i+1].text).group()})

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


