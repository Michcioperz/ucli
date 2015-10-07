from sys import exit
from src.arguments import get_parser

def main():
    args = get_parser().parse_args()

    if args.version:
        print ("no version yet")
        exit(0)
