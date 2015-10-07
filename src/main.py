from sys import exit
from . import arguments

def main():
    args = arguments.get_parser().parse_args()

    if args.version:
        print ("no version yet")
        exit(0)

    if "func" in vars(args).keys():
        args.func(args)
