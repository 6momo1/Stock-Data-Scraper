
"""

test module

"""
import sys
from Utils import Utils
from typing import List


class Program:
    def process_arguments(self, stock_symbols: List[str], csv: bool, aditional_headers: List[str] = None) -> None:

        stock_list_data = Utils().handle_user_input(stock_symbols)
        stock_df = Utils().dict_to_df(stock_list_data)

        # create csv file if true
        if csv:
            Utils().to_csv(stock_df, "stock_data.csv")

        sys.exit(1)


stock_symbols = ['msft', 'amzn']
aditional_headers = ['PE']
Program().process_arguments(stock_symbols=stock_symbols,
                            csv=False, aditional_headers=aditional_headers)
