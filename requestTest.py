import time
import requests
from bs4 import BeautifulSoup
import json
import re


class Scraper:

    def get_token_stats(self, token: str) -> dict:
        """
        Returns a dictionary containing 'token' and 'data'
        """
        try:
            url = 'https://finviz.com/quote.ashx?t={}'.format(token)
            headers = {
                'User-Agent': "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
            req = requests.get(url, headers=headers)

            print(req.status_code)
            if req.status_code != 200:
                raise Exception(
                    f"\n[ERROR] Token '{token}' is invalid.  Status code: {req.status_code} \n")
        except Exception as e:
            print(e)


Scraper().get_token_stats('pyp')
