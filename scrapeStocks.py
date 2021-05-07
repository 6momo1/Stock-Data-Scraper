"""

This module is to handle user arguments

"""
import argparse
from pprint import pprint
from typing import Optional
from typing import Sequence
import program


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
        '--headers',
        dest="headers",
        nargs='+',
        help="add aditional parameters to your dataset."
    )

    # name space format
    args = parser.parse_args(argv)

    # convert namespace to dict
    args = vars(args)

    # pprint(args)

    program.process_arguments(
        args['stock_symbols'], args['csv'], args['headers'])

    return 0


if __name__ == '__main__':
    exit(main())
