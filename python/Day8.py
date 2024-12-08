import logging
import argparse
import re

import submodules.utils as utils

logger = logging.getLogger(__name__)

antenna_dict = {}

def build_ant_dict(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] != '.':
                if input[i][j] not in antenna_dict.keys():
                    antenna_dict[input[i][j]] = []
                antenna_dict[input[i][j]].append((i, j))

antinodes = set()

def find_antinodes(ant_dict, input):
    for key in ant_dict.keys():
        if len(ant_dict[key]) <= 1:
            continue
        for i in range(len(ant_dict[key])):
            for j in range(i+1,len(ant_dict[key])):
                ydiff = ant_dict[key][i][0] - ant_dict[key][j][0]
                xdiff = ant_dict[key][i][1] - ant_dict[key][j][1]
                new_y = ant_dict[key][i][0]+ydiff
                new_x = ant_dict[key][i][1]+xdiff
                if new_y >= 0 and new_y < len(input) and new_x >=0 and new_x < len(input[0]):
                    antinodes.add((new_y, new_x))
                new_y = ant_dict[key][j][0]-ydiff
                new_x = ant_dict[key][j][1]-xdiff
                if new_y >= 0 and new_y < len(input) and new_x >=0 and new_x < len(input[0]):
                    antinodes.add((new_y, new_x))
    print(len(antinodes))

def find_more_antinodes(ant_dict, input):
    for key in ant_dict.keys():
        if len(ant_dict[key]) <= 1:
            continue
        for i in range(len(ant_dict[key])):
            for j in range(i+1,len(ant_dict[key])):
                ydiff = ant_dict[key][i][0] - ant_dict[key][j][0]
                xdiff = ant_dict[key][i][1] - ant_dict[key][j][1]
                y = ant_dict[key][i][0]     #+ydiff
                x = ant_dict[key][i][1]     #+xdiff
                while y >= 0 and y < len(input) and x >=0 and x < len(input[0]):
                    antinodes.add((y, x))
                    y += ydiff
                    x += xdiff
                y = ant_dict[key][j][0]     #-ydiff
                x = ant_dict[key][j][1]     #-xdiff
                while y >= 0 and y < len(input) and x >=0 and x < len(input[0]):
                    antinodes.add((y, x))
                    y -= ydiff
                    x -= xdiff
    print(len(antinodes))

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

    build_ant_dict(input)
    # find_antinodes(antenna_dict, input)
    find_more_antinodes(antenna_dict, input)
    # print(antenna_dict)