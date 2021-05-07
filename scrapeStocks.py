"""

This module is to handle user arguments

"""
import argparse
from pprint import pprint
from typing import Optional
from typing import Sequence
from program import Program


def main(argv: Optional[Sequence[str]] = None) -> int:

    parser = argparse.ArgumentParser()

    parser.add_argument(
        'stock_symbols',
        nargs='+',
        metavar='STOCK_SYMBOLS',
        help="One or more stock symbol to retrieve data."
    )

    parser.add_argument(
        '-c', '--csv',
        dest="csv",
        action="store_true",
        default=False,
        help="Create Comma-Seaperated Values (CSV) File from your selected stock symbols."
    )

    parser.add_argument(
        '--timeout',
        action='store',
        metavar='TIMEOUT',
        dest='timeout',
        default=0.25,
        help="Time (in seconds) to wait for response to requests a new stock symbol data. "
        "Default timeout is 0.25 seconds."
        "A longer timeout may cause a long delay to gather all results."
    )

    parser.add_argument(
        '--headers',
        dest="headers",
        nargs='+',
        help="Add aditional parameters to add to your dataset. Please choose from the following:  "
        "'ticker', 'Idx', 'PE', 'EPS_ttm', 'Insider_Own', 'Shs_Outstand', 'Perf_Week', 'Market_Cap', 'Forward_PE', 'EPS_next_Y', 'Insider_Trans', 'Shs_Float', 'Perf_Month', 'Income', 'PEG', 'EPS_next_Q', 'Inst_Own', 'Short_Float', 'Perf_Quarter', 'Sales', 'PS', 'EPS_this_Y', 'Inst_Trans', 'Short_Ratio', 'Perf_Half_Y', 'Booksh', 'PB', 'ROA', 'Target_Price', 'Perf_Year', 'Cashsh', 'PC', 'EPS_next_5Y', 'ROE', '52W_Range','Perf_YTD', 'Dividend', 'PFCF', 'EPS_past_5Y', 'ROI', '52W_High', 'Beta', 'Dividend_', 'Quick_Ratio', 'Sales_past_5Y', 'Gross_Margin', '52W_Low', 'ATR', 'Employees', 'Current_Ratio', 'Sales_QQ', 'Oper_Margin', 'RSI_14', 'Volatility', 'Optionable', 'DebtEq', 'EPS_QQ', 'Profit_Margin', 'Rel_Volume', 'Prev_Close', 'Shortable', 'LT_DebtEq', 'Earnings', 'Payout', 'Avg_Volume', 'Price', 'Recom', 'SMA20', 'SMA50', 'SMA200', 'Volume', 'Chg'"
    )

    # name-space format
    args = parser.parse_args(argv)

    # convert namespace to dict
    args = vars(args)

    pprint(args)

    Program().process_arguments(
        stock_symbols=args['stock_symbols'],
        csv=args['csv'],
        additional_headers=args['headers'],
        timeout=args['timeout']
    )

    return 0


if __name__ == '__main__':
    exit(main())
