# Stock-Data-Scraper

A Command Line too to scrape stock fundamental data from finiviz.

```console
$python3 scrapeStocks --help

usage: scrapeStocks.py [-h] [-c] [--timeout TIMEOUT] [--headers HEADERS [HEADERS ...]]
                       STOCK_SYMBOLS [STOCK_SYMBOLS ...]

positional arguments:
  STOCK_SYMBOLS         One or more stock symbol to retrieve data.

optional arguments:
  -h, --help            show this help message and exit
  -c, --csv             Create Comma-Seaperated Values (CSV) File from your selected stock symbols.
  --timeout TIMEOUT     Time (in seconds) to wait for response to requests a new stock symbol data. Default timeout is
                        0.25 seconds.A longer timeout may cause a long delay to gather all results.
  --headers HEADERS [HEADERS ...]
                        Add aditional parameters to add to your dataset. Please choose from the following: 'ticker',
                        'Idx', 'PE', 'EPS_ttm', 'Insider_Own', 'Shs_Outstand', 'Perf_Week', 'Market_Cap',
                        'Forward_PE', 'EPS_next_Y', 'Insider_Trans', 'Shs_Float', 'Perf_Month', 'Income', 'PEG',
                        'EPS_next_Q', 'Inst_Own', 'Short_Float', 'Perf_Quarter', 'Sales', 'PS', 'EPS_this_Y',
                        'Inst_Trans', 'Short_Ratio', 'Perf_Half_Y', 'Booksh', 'PB', 'ROA', 'Target_Price',
                        'Perf_Year', 'Cashsh', 'PC', 'EPS_next_5Y', 'ROE', '52W_Range','Perf_YTD', 'Dividend', 'PFCF',
                        'EPS_past_5Y', 'ROI', '52W_High', 'Beta', 'Dividend_', 'Quick_Ratio', 'Sales_past_5Y',
                        'Gross_Margin', '52W_Low', 'ATR', 'Employees', 'Current_Ratio', 'Sales_QQ', 'Oper_Margin',
                        'RSI_14', 'Volatility', 'Optionable', 'DebtEq', 'EPS_QQ', 'Profit_Margin', 'Rel_Volume',
                        'Prev_Close', 'Shortable', 'LT_DebtEq', 'Earnings', 'Payout', 'Avg_Volume', 'Price', 'Recom',
                        'SMA20', 'SMA50', 'SMA200', 'Volume', 'Chg'

```

To get data from a single stock:

```console
$ python3 scrapeStock aapl

Your requested headers are: Idx, Market_Cap, Income, Price

   token          Idx Market_Cap  Income   Price
0  AAPL  DJIA S&P500   2219.57B  76.31B  130.21

```

To get data for multiple stocks:

```console
$ python3 scrapeStock aapl googl tsla

Your requested headers are: Idx, Market_Cap, Income, Price

    token          Idx Market_Cap  Income    Price
0   AAPL  DJIA S&P500   2219.57B  76.31B   130.21
1  GOOGL      S&P 500   1614.48B  51.36B  2351.93
2   TSLA      S&P 500    645.38B   1.11B   672.37

```
