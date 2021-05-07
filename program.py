
"""

this module is to process the arguments passed by the user inputs from scrapeStocks

"""
import sys
from Utils import Utils
from typing import List


def process_arguments(stock_symbols: List[str], csv: bool, aditional_headers: List[str] = None) -> None:

    stock_list_data = Utils().handle_user_input(stock_symbols)
    stock_df = Utils().dict_to_df(stock_list_data)
    if csv:
        Utils().to_csv(stock_df, "file1")

    sys.exit(1)
