import logging
import argparse

import submodules.utils as utils

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(prog='Day1', description='Python solution to Advent of Code Day 1 puzzle')
    utils.common_args(parser=parser)
    args = parser.parse_args()
  
    logger.info(f"Opening {args.filename}")

    with open(args.filename, "r") as f:
        input = f.readlines()
    
    print(input)
