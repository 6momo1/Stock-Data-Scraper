
"""
This module contains functions to process the data retreived from the scraper function.

contains the functions:
    to_csv: creates a csv file
    dict_to_df: converts the dictionary object returned from Scraper function to pandas Datafram
    handle_user_input: process the user input

"""
from Scraper import Scraper
from typing import List
import pandas as pd
import os
import time


class Utils:

    def __init__(self):
        self.default_headers = ['Idx', 'Market_Cap', 'Income', 'Price']

    def to_csv(self, stock_list_df: pd.DataFrame, file_name: str = "stock_data.csv") -> None:
        """
        create a csv File from stock list df
        Note: could add the argument for directory

        """
        # current working directory
        cwd = os.getcwd()
        path = os.path.join(cwd, file_name + ".csv")
        print("\n CSV file saved to path: ", path)

        stock_list_df.to_csv(path, index=False)

    def dict_to_df(self, stock_list_data: List[dict]) -> pd.DataFrame:
        """
        Convert List of stock statistics dictionary to pandas dataframe
        """
        stock_list_df = pd.DataFrame.from_dict(stock_list_data)
        stock_list_df.set_index('token')
        print('\n', stock_list_df)
        return stock_list_df

    def handle_user_input(self, tokens: List[str],
                          headers: List[str] = [], timeout: float = 0.25) -> List[dict]:
        """
        returns a list of dictionary containing information about each entered token
        """
        # if user did not give headers, set headers to class default headers
        if headers == None:
            headers = self.default_headers
        else:
            headers = self.default_headers + headers

        print("\nYour requested headers are:", ', '.join(headers))

        stock_list_data = []  # stock list data to return

        for token in tokens:

            # returns {"token": token_Name, "data":{...}}
            token = token.upper()
            token_stats_dic = Scraper().get_token_stats(token)

            temp_dict = {}
            temp_dict['token'] = token

            try:
                # save the data that the user want returned
                for header in headers:

                    # parse the use headers and aditional headers, raise error if header is entered incorrectly
                    try:
                        temp_dict[header] = token_stats_dic['data'][header]
                    except Exception as e:
                        print('\n', e)
                        print(header, 'is incorrect, please enter a valid header. \n')

                stock_list_data.append(temp_dict)

                # wait time
                time.sleep(timeout)
            except:
                pass
        return stock_list_data
