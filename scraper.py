import time
import requests
from bs4 import BeautifulSoup
import json
import re


def urlify(s):
	"""
	his is a function that converts the dic to sql friendly syntax
	"""
    s = re.sub(r"[^\w\s]", '', s)
    s = re.sub(r"\s+", '_', s)
    if "Index" in s:
    	s = "Idx"
    if "Change" in s:
    	s = "Chg"
    return s

def get_ticker_info(token):
	"""
	Returns table data of from the give token as a dictionary
	"""
	try:
		url = 'https://finviz.com/quote.ashx?t={}'.format(token)
		headers = {'User-Agent':"Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
		req = requests.get(url, headers = headers)
		soup = BeautifulSoup(req.content, 'html.parser')
		table = soup.find_all("table", attrs = {'class':"snapshot-table2"})
		lst = []
		for row in range(12):
			for col in range(12):
				if (col % 2) == 0:
					lst.append(urlify(table[0].find_all('tr')[row].find_all('td')[col].text))
				else:
					lst.append(table[0].find_all('tr')[row].find_all('td')[col].text)

		dic = {"Token": token}

		temp_dic = {lst[i]:lst[i+1] for i in range(0,len(lst),2)}
		dic.update(temp_dic)
		return dic
	except Exception as e:
		print(e)

