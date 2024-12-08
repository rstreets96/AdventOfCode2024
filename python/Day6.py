import logging
import argparse
import re

import submodules.utils as utils

logger = logging.getLogger(__name__)



def travel(input, row, col, new_blocks):
    if input[row][col] == '^':
        if row == 0:
            return input, row-1, col, new_blocks
        if input[row-1][col] == '#':
            input[row][col+1] = '>'
            return input, row, col+1, new_blocks
        else:
            if row != 0:
                for i in range(col, len(input[row])):
                    if input[row][i] == '#':
                        break
                    if input[row][i] == '>':
                        new_blocks.add((row-1, col))
                        break
            input[row-1][col] = '^'
            return input, row-1, col, new_blocks
    elif input[row][col] == '>':
        if col == len(input[row]) - 1:
            return input, row, col+1, new_blocks
        if input[row][col+1] == '#':
            input[row+1][col] = 'V'
            return input, row+1, col, new_blocks
        else:
            if col != len(input[row])-1:
                for i in range(row, len(input)):
                    if input[i][col] == '#':
                        break
                    if input[i][col] == 'V':
                        new_blocks.add((row, col+1))
                        break
            input[row][col+1] = '>'
            return input, row, col+1, new_blocks
    elif input[row][col] == 'V':
        if row == len(input)-1:
            return input, row+1, col, new_blocks
        if input[row+1][col] == '#':
            input[row][col-1] = '<'
            return input, row, col-1, new_blocks
        else:
            if row != len(input)-1:
                for i in range(col, 0):
                    if input[row][i] == '#':
                        break
                    if input[row][i] == '<':
                        new_blocks.add((row+1, col))
                        break
            input[row+1][col] = 'V'
            return input, row+1, col, new_blocks
    elif input[row][col] == '<':
        if col == 0:
            return input, row, col-1
        if input[row][col-1] == '#':
            input[row-1][col] = '^'
            return input, row-1, col, new_blocks
        else:
            if col != 0:
                for i in range(row, 0):
                    if input[i][col] == '#':
                        break
                    if input[i][col] == '^':
                        new_blocks.add((row, col-1))
                        break
            input[row][col-1] = '<'
            return input, row, col-1, new_blocks
    
            

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
    done = False
    new_blocks = set()
    for i in range(len(input)-1):  
        for j in range(len(input[i])-1):
            if input[i][j] == '^':
                while i >= 0 and j >= 0 and i < len(input) and j < len(input[i]):
                    input, i, j, new_blocks = travel(input, i, j, new_blocks)
                done = True
                for row in range(len(input)):
                    for col in range(len(input[row])):
                        if input[row][col] in ['>', '<', '^', 'V']:
                            sum += 1
                print(new_blocks)
                print(sum, len(new_blocks))
                break
        if done:
            break
