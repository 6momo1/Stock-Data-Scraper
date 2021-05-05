# command line interface
# Main

from scraper import Scraper

scraper = Scraper()

tokens = ['msft']
default_headers = ['Idx', 'Market_Cap', 'Income', 'Price']
for token in tokens:
    tokenStats = scraper.get_ticker_stats(token)

    return_data = {}
    for header in default_headers:
        return_data[header] = tokenStats['data'][header]

    print(tokenStats['Token'], return_data)

# print(scraper.get_header_list())
