import argparse
import sys
from sherloock import Sherloock

def main():
    parser = argparse.ArgumentParser(
        description="Sherloock: Stochastic Hybrid Efficient Reasoning Layered Object-Oriented Command"
    )
    parser.add_argument(
        'query',
        type=str,
        nargs='+',
        help='El comando o consulta para el motor Sherloock'
    )

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    full_query = " ".join(args.query)

    sherloock = Sherloock()
    result = sherloock.reason(full_query)
    print(result)
