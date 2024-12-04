import logging
import argparse
import re

import submodules.utils as utils

logger = logging.getLogger(__name__)

# def find_closest(num_list, num):
#     if num < num_list[0]:
#         return None
#     elif num > num_list[-1]:
#         return num_list[-1]
#     timeout = 0
#     i = len(num_list) // 2
#     while not (num_list[i] < num < num_list[i+1]) and timeout < 20:
#         if num > num_list[i]:
#             i += (len(num_list) - i + 1) // 2
#         else:
#             i = (i - 1) // 2
#         timeout += 1

#     if num_list[i] < num < num_list[i+1]:
#         logger.debug(f"Found! {i}, {num_list[i]}, {num}")
#         return num_list[i]
#     else:
#         logger.debug(f"Not Found! List: {num_list} Num: {num}")
#         return None

def find_closest(num_list, num):
    if num < num_list[0]:
        return None
    elif num > num_list[-1]:
        return num_list[-1]
    for i in range(len(num_list)):
        if num_list[i] < num < num_list[i+1]:
            return num_list[i]
    return None

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(prog='Day3', description='Python solution to Advent of Code Day 3 puzzle')
    utils.common_args(parser=parser)
    args = parser.parse_args()
  
    logger.debug(f"Opening {args.filename}")

    with open(args.filename, "r") as f:
        input = f.read()
    
    # pattern = r'mul\(\d{1,3},\d{1,3}\)'
    # matches = re.findall(pattern, input)

    # sum = 0
    # for match in matches:
    #     pair = match[4:-1].split(',')
    #     sum += int(pair[0]) * int(pair[1])
    # logger.info(sum)
    
    pattern_mul = r'mul\(\d{1,3},\d{1,3}\)'
    pattern_do = r'do\(\)'
    pattern_dont = r'don\'t\(\)'

    mul_matches = re.finditer(pattern_mul, input)
    do_matches = re.finditer(pattern_do, input)
    dont_matches = re.finditer(pattern_dont, input)
    do_idxs = []
    dont_idxs = []
    sum = 0

    for match in do_matches:
        do_idxs.append(match.span()[0])
    for match in dont_matches:
        dont_idxs.append(match.span()[0])
    for match in mul_matches:
        prev_do_idx = find_closest(do_idxs, match.span()[0])
        if prev_do_idx == None:
            prev_do_idx = 0
        prev_dont_idx = find_closest(dont_idxs, match.span()[0])
        if prev_dont_idx == None:
            prev_dont_idx = 0
        logger.debug(f"Prev do(): {prev_do_idx}. Prev don't(): {prev_dont_idx}, Match: {match.span()[0]}, {sum}")
        if prev_do_idx > prev_dont_idx or prev_dont_idx == 0:
            pair = match.group()[4:-1].split(',')
            sum += int(pair[0]) * int(pair[1])
    logger.info(sum)