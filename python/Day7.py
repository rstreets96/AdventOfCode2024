import logging
import argparse
import re

import submodules.utils as utils

logger = logging.getLogger(__name__)
SUBTRACTION = 0
DIVISION = 1

def valid_eq(line):
    totals = []
    totals.append((int(line[0][:-1]), None))
    i = len(line)-1
    while i >= 1:
        for j in range(len(totals)):
            if totals[j][0] % int(line[i]) == 0:
                totals.append((totals[j][0]-int(line[i]), SUBTRACTION))
                totals[j] = (totals[j][0] // int(line[i]), DIVISION)
            else:
                totals[j] = (totals[j][0] - int(line[i]), SUBTRACTION)
        i -=1
    for total in totals:
        if (total[1] == SUBTRACTION and total[0] == 0) or (total[1] == DIVISION and total[0] == 1):
            return int(line[0][:-1])
    return 0


def new_op(line):
    curr = []
    curr.append(int(line[1]))
    for i in range(2, len(line)):
        fronts = len(curr)
        for j in range(fronts):
                tot = curr.pop(0)
                curr.append(tot * int(line[i]))
                curr.append((tot * (10 ** len(line[i])))+int(line[i]))
                curr.append(tot + int(line[i]))
        
    if int(line[0][:-1]) in curr:
        return int(line[0][:-1])
    else:
        return 0
                


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(prog='Day3', description='Python solution to Advent of Code Day 3 puzzle')
    utils.common_args(parser=parser)
    args = parser.parse_args()
  
    logger.debug(f"Opening {args.filename}")

    with open(args.filename, "r") as f:
        input = f.readlines()
    
    for i in range(len(input)):
        input[i] = input[i].split()

    # sum = 0
    # for i in range(len(input)):
    #     sum +=valid_eq(input[i])
    # print(sum)

    
    sum = 0
    for i in range(len(input)):
        sum +=new_op(input[i])
    print(sum)