import time
import requests
from bs4 import BeautifulSoup
import json
import re
import datetime
import json


FILE = "main.db"

def urlify(s):
    s = re.sub(r"[^\w\s]", '', s)
    s = re.sub(r"\s+", '_', s)
    if "Index" in s:
    	s = "Idx"
    if "Change" in s:
    	s = "Chg"
    return s


def valid_ticker(page):
	"""
	Check if ticker is valid
	"""
	mydivs = page.findAll("div", {"class": "container"})
	if "No results found" in mydivs[0].text:
		return False
	else:
		return True


def get_all(ticker):
	"""
	Returns a a tuple containing a list of [ticker, page], and a dictionary containing the stats
	:params: str
	:return: tuple
	"""
	page = get_page(ticker) #returns li[ticker,soup]
	stats = get_stats(page[0],page[1]) #returns dic
	print(f"HTML and stats for {ticker} has been returned.")
	return (page,stats)



def get_page(ticker):
	"""
	Returns dictionary containg the ticker, and the html of a stock
	li[ticker, soup]
	:params ticker: str
	:return: list
	"""
	ticker = ticker.upper()
	try:
		url = 'https://finviz.com/quote.ashx?t={}'.format(ticker)
		headers = {'User-Agent':"Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
		req = requests.get(url, headers = headers)
		soup = BeautifulSoup(req.content, 'html.parser')

		#Raise exception if Ticker is invalid
		if (valid_ticker(soup) == False) or (req.status_code != 200):
			return Exception("The ticker {} is invalid.".format(ticker))

		li = [ticker,f"""{soup}"""]

		print(f"Page for {ticker} has been retrieved.")
		return li

	except Exception as e:
		print(e)




def get_stats(ticker, soup):
	"""
	Returns table data of from the give ticker as a dictionary
	:params ticker: str
	:params soup: bs4
	:return: dict
	"""
	try:
		soup = BeautifulSoup(soup, 'html.parser')
		table = soup.find_all("table", attrs = {'class':"snapshot-table2"})
		lst = []
		for row in range(12):
			for col in range(12):
				if (col % 2) == 0:
					lst.append(urlify(table[0].find_all('tr')[row].find_all('td')[col].text))
				else:
					lst.append(table[0].find_all('tr')[row].find_all('td')[col].text)

		dic = {"ticker": ticker}

		temp_dic = {lst[i]:lst[i+1] for i in range(0,len(lst),2)}
		dic.update(temp_dic)

		print(f"Stats for {ticker} has been parsed")
		return dic
	except Exception as e:
		print(e)


