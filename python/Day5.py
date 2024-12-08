import logging
import argparse
import re

import submodules.utils as utils

logger = logging.getLogger(__name__)

not_after_dict = {}

def build_rule_dict(input):
    for i in range(len(input)):
        line = input[i]
        if "|" in line:
            line = line[:-1].split("|")
            if line[0] not in not_after_dict.keys():
                not_after_dict[line[0]] = []                
            not_after_dict[line[0]].append(line[1])
        else:
            return i

def valid_print(print):
    print = print[:-1].split(',')
    seen = set()
    for num in print:
        for illegal in not_after_dict[num]:
            if illegal in seen:
                return 0
        seen.add(num)
    return int(print[len(print) // 2])

before_dict = {}
after_dict = {}
def build_before_after_dict(input):
    for i in range(len(input)):
        line = input[i]
        if "|" in line:
            line = line[:-1].split("|")
            if line[0] not in after_dict.keys():
                after_dict[line[0]] = []                
            after_dict[line[0]].append(line[1])
            if line[1] not in before_dict.keys():
                before_dict[line[1]] = []
                before_dict[line[1]].append(line[0])
        else:
            return i

def check_rules(num, seen):
    for after_num in after_dict[num]:
            if after_num in seen:
                return True
    return False

def fix_line(line):
    pass

def fixed_print(line):
    line = line[:-1].split(',')
    needs_fix = False
    seen = set()
    for i in range(len(line)):
        num = line[i]
        if check_rules(num, seen):
            needs_fix = True
            break
        seen.add(num)
    if needs_fix:
        print(line)
        fix_line(line)
        return 0
    else:
        return int(line[len(line) // 2])

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(prog='Day3', description='Python solution to Advent of Code Day 3 puzzle')
    utils.common_args(parser=parser)
    args = parser.parse_args()
  
    logger.debug(f"Opening {args.filename}")

    with open(args.filename, "r") as f:
        input = f.readlines()
    
    # prints_start = build_rule_dict(input)

    # sum = 0
    # for i in range(prints_start+1, len(input)):
    #     sum += valid_print(input[i])
    #     print(sum, input[i])
    # print(sum)

    prints_start = build_before_after_dict(input)
    sum = 0
    for i in range(prints_start+1, len(input)):
        sum += fixed_print(input[i])
        # print(sum, input[i])
    print(sum)