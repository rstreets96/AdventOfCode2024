import logging
import argparse
import re

import submodules.utils as utils

logger = logging.getLogger(__name__)

dirs = [(0, 1), (0, -1), (1,0), (-1, 0)]

def trailhead_score(graph, row, col, val, nines_set):
    if row < 0 or row > len(graph)-1 or col < 0 or col > len(graph)-1:
        return 0
    if int(graph[row][col]) != val:
        return 0
    if val == 9:
        nines_set.add((row, col))
        return 1
    for dir in dirs:
        trailhead_score(graph,row+dir[0], col+dir[1], val+1, nines_set)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(prog='Day3', description='Python solution to Advent of Code Day 3 puzzle')
    utils.common_args(parser=parser)
    args = parser.parse_args()
  
    logger.debug(f"Opening {args.filename}")

    with open(args.filename, "r") as f:
        input = f.readlines()

    for i in range(len(input)):
        input[i] = list(input[i])[:-1]

    sum = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '0':
                nines_set = set()
                trailhead_score(input, i, j, 0, nines_set)
                print(i, j, len(nines_set))
                sum += len(nines_set)
    print(sum)