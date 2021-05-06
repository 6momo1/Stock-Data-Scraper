# command line interface
# Main
import pprint
from scraper import Scraper
from typing import List


class Utils:

    def __init__(self):
        self.default_headers = ['Idx', 'Market_Cap', 'Income', 'Price']

    def print_data(self, stock_list):
        print('test')
        return

    def dic_to_list(self, stock_list):
        pass

    def handle_user_input(self, token: List[str], headers: List[str] = []) -> List[dict]:
        """
        returns a list of dictionary containing information about each entered token
        """

        # if user did not give headers, set headers to default headers
        if headers == []:
            headers = self.default_headers

        print(headers)
        stock_list_data = []  # stock list data to return

        for token in tokens:

            # returns {"token": token_Name, "data":{...}}
            token_stats_dic = scraper.get_token_stats(token)

            temp_dict = {}

            # save the data that the user want returned
            for header in headers:
                temp_dict[header] = token_stats_dic['data'][header]

            temp_dict['token'] = token
            stock_list_data.append(temp_dict)

        return stock_list_data


scraper = Scraper()
Utils = Utils()

tokens = ['msft', 'aapl']

stock_list_data = Utils.handle_user_input(tokens)

print(stock_list_data)
