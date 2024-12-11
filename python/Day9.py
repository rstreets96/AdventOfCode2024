import logging
import argparse
import re

import submodules.utils as utils

logger = logging.getLogger(__name__)

def disk_map_list(input):
    file_map = []
    file_idx = 0
    position = 0
    is_space = False
    for i in range(len(input)):
        if not is_space:
            for j in range(position, position + int(input[i])):
                file_map.append(file_idx)
            
        else:
            for j in range(position, position + int(input[i])):
                file_map.append('.')
            file_idx +=1
        is_space = not is_space
        position += int(input[i])
    return file_map


def checksum_and_move_files(map):
    # print(map)
    sum = 0
    right = len(map) - 1
    for i in range(len(map)):
        # print(sum, i, map[i])
        if map[i] == '.' and i < right:
            while map[right] == '.' and i < right:
                right -= 1
            if i < right:
                map[i] = map[right]
                map[right] = '.'
        if map[i] != '.':
            sum += map[i] * i
    # print(map)
    return sum


class FileSpace():
    def __init__(self, start, length, num, isEmpty):
        self.start_idx = int(start)
        self.file_len = int(length)
        self.file_num = int(num)
        self.is_empty = int(isEmpty)
 

def disk_map_files(input):
    files = []
    file_idx = 0
    position = 0
    is_space = False
    for i in range(len(input)):
        files.append(FileSpace(position, input[i], file_idx, is_space))
        if is_space:
            file_idx +=1
        is_space = not is_space
        position += int(input[i])
    return files

def move_files(files):
    i = len(files)-1
    sum = 0
    while i >= 0:
        if not files[i].is_empty and files[i].file_len != 0:
            for j in range(len(files)):
                if j >= i:
                    break
                if files[j].is_empty and (files[j].file_len >= files[i].file_len):
                    if(files[j].file_len > files[i].file_len):
                        files.insert(j+1, FileSpace(files[j].start_idx + files[i].file_len, files[j].file_len - files[i].file_len, 0, True))
                        i += 1
                    files[j].file_num = files[i].file_num
                    files[j].file_len = files[i].file_len
                    files[j].is_empty = False
                    files.pop(i)
                    # print(i, files[i].start_idx, files[i].file_len, files[i].file_num, files[i].is_empty)
                    # print(j, files[j].start_idx, files[j].file_len, files[j].file_num, files[j].is_empty)
                    # print(j+1, files[j+1].start_idx, files[j+1].file_len, files[j+1].file_num, files[j+1].is_empty)
                    # print('\n')
                    break
        i -= 1
    for k in range(len(files)):
        if not files[k].is_empty:
            for l in range(files[k].start_idx, files[k].start_idx + files[k].file_len):
                # print(files[k].file_num, l)
                sum += files[k].file_num * l
    print(sum)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(prog='Day3', description='Python solution to Advent of Code Day 3 puzzle')
    utils.common_args(parser=parser)
    args = parser.parse_args()
  
    logger.debug(f"Opening {args.filename}")

    with open(args.filename, "r") as f:
        input = f.read()
    
    input = list(input)[:-1]
    # file_map = disk_map_list(input)

    # print(checksum_and_move_files(file_map))
    files = disk_map_files(input)
    # for file in files:
    #     print(file.start_idx, file.file_len, file.file_num, file.is_empty)
    # for file in files[:100]:
    #     print(file.start_idx, file.file_num, file.file_len)
    move_files(files)
    # for file in files[:100]:
    #     print(file.start_idx, file.file_num, file.file_len)
    
    # move_files(disk_map_files(input))
