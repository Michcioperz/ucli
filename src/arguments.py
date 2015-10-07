import argparse

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="be more verbose", action="store_true")
    parser.add_argument("--version", help="show version", action="store_true")

    return parser
