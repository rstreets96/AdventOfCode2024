import argparse

def common_args(parser):
    parser.add_argument("-f", "--filename", type=str, required=True, help="The relative filepath to the input file")
    parser.add_argument("-p", "--part-nums", type=int, nargs='+', default=[1, 2], help="Choose which parts of the problem to execute")