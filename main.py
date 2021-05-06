from Utils import Utils
from Scraper import Scraper


scraper = Scraper()
Utils = Utils()

tokens = ['mst', 'aapl', 'pypl', 'GM', 'abnb', 'spot']

stock_list_data = Utils.handle_user_input(tokens)
stock_df = Utils.dict_to_df(stock_list_data)
Utils.to_csv(stock_df, "file1")
