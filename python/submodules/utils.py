import argparse

def common_args(parser):
    parser.add_argument("-f", "--filename", type=str, required=True, help="The relative filepath to the input file")