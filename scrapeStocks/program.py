
"""

this module is to process the arguments passed by the user inputs from scrapeStocks

"""
import sys
from Utils import Utils
from typing import List


class Program:
    def process_arguments(
            self, stock_symbols: List[str], csv: bool, additional_headers: List[str] = None, timeout: float = 0.25) -> None:

        # Scrape the data
        stock_list_data = Utils().handle_user_input(
            tokens=stock_symbols, headers=additional_headers, timeout=timeout)

        # Convert it to a Pandas DataFrame Object
        stock_df = Utils().dict_to_df(stock_list_data)

        # Create a csv file requested
        if csv:
            Utils().to_csv(stock_df, "stock_data")

        sys.exit(1)
