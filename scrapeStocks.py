
import argparse
from pprint import pprint
from typing import Optional
from typing import Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'stock_symbol',
        nargs='+',
        metavar='STOCK_SYMBOL',
        help="One or more stock symbols to retrieve data."
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

    args = parser.parse_args(argv)

    pprint(vars(args))
    return 0


if __name__ == '__main__':
    exit(main())
