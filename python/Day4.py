import logging
import argparse
import re

import submodules.utils as utils

logger = logging.getLogger(__name__)

DIRECTION_ANY = 0
DIRECTION_RIGHT = 1
DIRECTION_LEFT = 2
DIRECTION_UP = 3
DIRECTION_DOWN = 4
DIRECTION_RIGHT_UP = 5
DIRECTION_RIGHT_DOWN = 6
DIRECTION_LEFT_UP = 7
DIRECTION_LEFT_DOWN = 8

letter_dict = {
    1 : 'X',
    2 : 'M',
    3 : 'A',
    4 : 'S',
}

def dfs(graph, row, col, letter_num, dir):
    if row >= len(graph) or row < 0 or col >= len(graph[0]) or col < 0:
        return 0
    # print(row, col, graph[row][col])
    if graph[row][col] != letter_dict[letter_num]:
        return 0
    if letter_dict[letter_num] == 'S':
        return 1
    ret = 0
    if dir == DIRECTION_ANY:
        ret = dfs(graph, row+1, col, letter_num+1, DIRECTION_DOWN) + \
            dfs(graph, row+1, col+1, letter_num+1, DIRECTION_RIGHT_DOWN) + \
            dfs(graph, row+1, col-1, letter_num+1, DIRECTION_LEFT_DOWN) + \
            dfs(graph, row, col+1, letter_num+1, DIRECTION_RIGHT) + \
            dfs(graph, row, col-1, letter_num+1, DIRECTION_LEFT) + \
            dfs(graph, row-1, col, letter_num+1, DIRECTION_UP) + \
            dfs(graph, row-1, col+1, letter_num+1, DIRECTION_RIGHT_UP) + \
            dfs(graph, row-1, col-1, letter_num+1, DIRECTION_LEFT_UP)
    elif dir == DIRECTION_DOWN:
        ret = dfs(graph, row+1, col, letter_num+1, DIRECTION_DOWN)
    elif dir == DIRECTION_RIGHT_DOWN:
        ret = dfs(graph, row+1, col+1, letter_num+1, DIRECTION_RIGHT_DOWN)
    elif dir == DIRECTION_LEFT_DOWN:
        ret = dfs(graph, row+1, col-1, letter_num+1, DIRECTION_LEFT_DOWN)
    elif dir == DIRECTION_RIGHT_UP:
        ret = dfs(graph, row-1, col+1, letter_num+1, DIRECTION_RIGHT_UP)
    elif dir == DIRECTION_LEFT_UP:
        ret = dfs(graph, row-1, col-1, letter_num+1, DIRECTION_LEFT_UP)
    elif dir == DIRECTION_RIGHT:
        ret = dfs(graph, row, col+1, letter_num+1, DIRECTION_RIGHT)
    elif dir == DIRECTION_LEFT:
        ret = dfs(graph, row, col-1, letter_num+1, DIRECTION_LEFT)
    elif dir == DIRECTION_UP:
        ret = dfs(graph, row-1, col, letter_num+1, DIRECTION_UP)
    return ret

def find_x_mas(graph, row, col):
    if row == 0 or col == 0 or row == len(graph)-1 or col == len(graph[0])-1:
        return False
    if graph[row][col] != 'A':
        return False
    corners = []
    corners_dict = {'M':[], 'S':[]}
    corners.append(graph[row-1][col-1])
    corners.append(graph[row-1][col+1])
    corners.append(graph[row+1][col+1])
    corners.append(graph[row+1][col-1])
    for i in range(len(corners)):
        if corners[i] == 'M':
            corners_dict['M'].append(i)
        if corners[i] == 'S':
            corners_dict['S'].append(i)
    if len(corners_dict['M']) == 2 and len(corners_dict['S']) == 2:
        if corners_dict['M'][0] == 0 and corners_dict['M'][1] == 2:
            return False
        if corners_dict['M'][0] == 1 and corners_dict['M'][1] == 3:
            return False
        print(row, col, graph[row][col], corners)
        return True
    return False

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
        for j in range(len(input[0])):
            if find_x_mas(input, i, j):
                sum += 1
            # sum += dfs(input, i, j, 1, DIRECTION_ANY)
    print(sum)
    