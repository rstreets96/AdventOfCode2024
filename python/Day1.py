import logging
import argparse
import numpy as np

import submodules.utils as utils

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(prog='Day1', description='Python solution to Advent of Code Day 1 puzzle')
    utils.common_args(parser=parser)
    args = parser.parse_args()
  
    logger.debug(f"Opening {args.filename}")

    with open(args.filename, "r") as f:
        input = f.readlines()
    
    for i in range(len(input)):
        input[i] = input[i].split()
    
    input_array = np.array(input)
    lists = input_array.T

    # Part 1
    #************************************************************
    if 1 in args.part_nums:
        list_copy = lists
        list_copy[0].sort()
        list_copy[1].sort()
        sum = 0
        for i in range(len(list_copy[0])):
            sum += abs(int(list_copy[0][i]) - int(list_copy[1][i]))
        logger.info(f"Solution to part 1: {sum}")

    # Part 2
    #************************************************************
    if 2 in args.part_nums:
        list2_dict = {}
        for item in lists[1]:
            if item in list2_dict.keys():
                list2_dict[item] +=1
            else:
                list2_dict[item] = 1
        sum = 0
        for item in lists[0]:
            if item in list2_dict.keys():
                sum += int(item) * list2_dict[item]
        logger.info(f"Solution to part 2: {sum}")
