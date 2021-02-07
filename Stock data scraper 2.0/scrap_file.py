import time
import requests
from bs4 import BeautifulSoup
import json
import re
import datetime
import json

page = open("error_page.txt","r")
aapl = open("aapl_page.txt","r")
error_page = BeautifulSoup(page, 'html.parser')
aapl = BeautifulSoup(aapl, 'html.parser')

def valid_ticker(page,request_obj):
	"""Check if ticker is valid"""
	mydivs = page.findAll("div", {"class": "container"})
	if ("No results found" in mydivs[0].text) or (request_obj.status_code != 200):
		return False
	else:
		return True



