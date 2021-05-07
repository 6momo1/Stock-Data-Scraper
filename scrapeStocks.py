
import argparse
from pprint import pprint
from typing import Optional
from typing import Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-c', '--csv',
        dest="csv",
        default="stock_data.csv",
        help="Create Comma-Seaperated Values (CSV) File from your selected stock symbols."
    )

    pprint(vars(argv))
    return 0


if __name__ == '__main__':
    exit(main())
