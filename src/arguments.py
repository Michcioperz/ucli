import argparse

from . import courses

def get_parser():
    parser = argparse.ArgumentParser()


    parser.add_argument("-a", "--address", required=True,
            help="serwer address")

    parser.add_argument("-v", "--verbose", action="store_true",
            help="be more verbose")

    parser.add_argument("--version", 
            help="show version", action="store_true")


    subparser = parser.add_subparsers(title="command")
    add_courses_parser(subparser)

    return parser

def add_courses_parser(parent):
    parser = parent.add_parser("courses")
    subparser = parser.add_subparsers(title="command")


    search = subparser.add_parser("search", 
            description="search for a given name in courses list and list result"
                        ", no more than 100 results can be shown")

    search.add_argument("name", 
            help="course name or a part of it")

    search.add_argument("-c", "--count", default=8, type=int, metavar='n',
            help="number of results to show, set to 8 by default")

    search.add_argument("-s", "--start", default=0, type=int, metavar='n',
            help="show results starting from n-th result (counting from 0)")

    search.set_defaults(func=courses.do_search)


    #TODO:
    info = subparser.add_parser("info")
    uints = subparser.add_parser("units")
