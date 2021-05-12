# Stock-Data-Scraper

A Command Line too to scrape stock fundamental data from finiviz.

## Usage

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

## Examples:

### Get Data:

To get data from a single stock:

###### For example, get data for the stock Apple:

```console
$ python3 scrapeStock aapl

Your requested headers are: Idx, Market_Cap, Income, Price

   token          Idx Market_Cap  Income   Price
0  AAPL  DJIA S&P500   2219.57B  76.31B  130.21

```

To get data for multiple stocks:

```console
$ python3 scrapeStocks aapl googl tsla


Your requested headers are: Idx, Market_Cap, Income, Price

    token          Idx Market_Cap  Income    Price
0   AAPL  DJIA S&P500   2219.57B  76.31B   130.21
1  GOOGL      S&P 500   1614.48B  51.36B  2351.93
2   TSLA      S&P 500    645.38B   1.11B   672.37

```

### Save as CSV

Save the data as a CSV file:

```console
$ python3 scrapeStocks.py aapl googl tsla --csv


Your requested headers are: Idx, Market_Cap, Income, Price

    token          Idx Market_Cap  Income    Price
0   AAPL  DJIA S&P500   2219.57B  76.31B   130.21
1  GOOGL      S&P 500   1614.48B  51.36B  2351.93
2   TSLA      S&P 500    645.38B   1.11B   672.37

 CSV file saved to path:  YOUR/CURRENT/WORKING/DIRECTORY/stock_data.csv
```

### Set Timout

Set wait time between scraping each stock.
Faster time may lead to higher chances of getting errors.

```console
$ python3 scrapeStocks.py aapl --timeout 0.5
```

### Additional Stock Data Output

Add additonal information to your dataset:

these additional headers can be selected from `--headers` option.

###### For example, if you want aditional information such as the PE ration of a stock, Profit Margin, or wether or not a stock

###### has dividends, you can add them as parameters.

```console
$ python3 scrapeStocks.py aapl googl tsla --headers PE Volume Profit_Margin Dividend_

Your requested headers are: Idx, Market_Cap, Income, Price, PE, Volume, Profit_Margin, Dividend_

    token          Idx Market_Cap  Income    Price      PE      Volume Profit_Margin Dividend_
0   AAPL  DJIA S&P500   2219.57B  76.31B   130.21   29.22  78,339,673        23.50%     0.68%
1  GOOGL      S&P 500   1614.48B  51.36B  2351.93   30.38   1,444,167        26.10%         -
2   TSLA      S&P 500    645.38B   1.11B   672.37  677.79  23,236,272         3.10%         -
```

more features to implement:
retrieve stock chart data
retrieve stock news data
