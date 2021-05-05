import time
import requests
from bs4 import BeautifulSoup
import json
import re


class Scraper:

    def __init__(self):
        self.header_list = ['ticker', 'Idx', 'PE', 'EPS_ttm', 'Insider_Own', 'Shs_Outstand', 'Perf_Week', 'Market_Cap', 'Forward_PE', 'EPS_next_Y', 'Insider_Trans', 'Shs_Float', 'Perf_Month', 'Income', 'PEG', 'EPS_next_Q', 'Inst_Own', 'Short_Float', 'Perf_Quarter', 'Sales', 'PS', 'EPS_this_Y', 'Inst_Trans', 'Short_Ratio', 'Perf_Half_Y', 'Booksh', 'PB', 'ROA', 'Target_Price', 'Perf_Year', 'Cashsh', 'PC', 'EPS_next_5Y', 'ROE', '52W_Range',
                            'Perf_YTD', 'Dividend', 'PFCF', 'EPS_past_5Y', 'ROI', '52W_High', 'Beta', 'Dividend_', 'Quick_Ratio', 'Sales_past_5Y', 'Gross_Margin', '52W_Low', 'ATR', 'Employees', 'Current_Ratio', 'Sales_QQ', 'Oper_Margin', 'RSI_14', 'Volatility', 'Optionable', 'DebtEq', 'EPS_QQ', 'Profit_Margin', 'Rel_Volume', 'Prev_Close', 'Shortable', 'LT_DebtEq', 'Earnings', 'Payout', 'Avg_Volume', 'Price', 'Recom', 'SMA20', 'SMA50', 'SMA200', 'Volume', 'Chg']

    def get_header_list(self):
        return self.header_list

    def urlify(self, s):
        """
        this is a function that converts the dic to sql friendly syntax
        """
        s = re.sub(r"[^\w\s]", '', s)
        s = re.sub(r"\s+", '_', s)
        if "Index" in s:
            s = "Idx"
        if "Change" in s:
            s = "Chg"

        return s

    def get_ticker_stats(self, token):
        """
        Returns table data of from the give token as a dictionary
        """
        try:
            url = 'https://finviz.com/quote.ashx?t={}'.format(token)
            headers = {
                'User-Agent': "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
            req = requests.get(url, headers=headers)

            # retrieve HTML page
            soup = BeautifulSoup(req.content, 'html.parser')
            table = soup.find_all("table", attrs={'class': "snapshot-table2"})

            # extract the data from HTML
            lst = []
            for row in range(12):
                for col in range(12):
                    if (col % 2) == 0:
                        lst.append(self.urlify(table[0].find_all('tr')[
                                   row].find_all('td')[col].text))
                    else:
                        lst.append(table[0].find_all('tr')[
                                   row].find_all('td')[col].text)

                        # create a dictionary to return
            dic = {"Token": token}
            temp_dic = {lst[i]: lst[i+1] for i in range(0, len(lst), 2)}
            dic["data"] = temp_dic

            return dic

        except Exception as e:
            print(e)
