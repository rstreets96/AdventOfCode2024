import logging
import argparse
import numpy as np

import submodules.utils as utils

logger = logging.getLogger(__name__)

def run_report(report):
    diffs = []
    skip_diffs = []
    inc_dec_cnt = 0

    report = report.split()
    for i in range(len(report) - 1):
        step = int(report[i]) - int(report[i+1])
        if step > 0:
            inc_dec_cnt += 1
        if step < 0:
            inc_dec_cnt -= 1
        diffs.append(step)
        if i < len(report) - 2:
            skip_diffs.append(int(report[i]) - int(report[i+2]))

    bad_idxs = []
    if inc_dec_cnt > 0:
        for i in range(len(diffs)):
            if diffs[i] <= 0 or diffs[i] > 3:
                bad_idxs.append(i)
    elif inc_dec_cnt < 0:
        for i in range(len(diffs)):
            if diffs[i] >= 0 or diffs[i] < -3:
                bad_idxs.append(i)
    else:
        return False
    
    if len(bad_idxs) == 0:
        return True
    elif len(bad_idxs) > 2:
        return False
    elif len(bad_idxs) == 2 and (bad_idxs[1] - bad_idxs[0]) > 1:
        return False
    elif len(bad_idxs) == 2 and inc_dec_cnt > 0:
        if skip_diffs[bad_idxs[0]] <= 3 and skip_diffs[bad_idxs[0]] > 0:
            return True
    elif len(bad_idxs) == 2 and inc_dec_cnt < 0:
        if skip_diffs[bad_idxs[0]] >= -3 and skip_diffs[bad_idxs[0]] < 0:
            return True
    elif len(bad_idxs) == 1:
        logger.debug(f"{report} - {bad_idxs}")
        if bad_idxs[0] == 0 or bad_idxs[0] == len(report) - 2:
            return True
        elif inc_dec_cnt > 0:
            if skip_diffs[bad_idxs[0]] <= 3 and skip_diffs[bad_idxs[0]] > 0:
                return True
        elif inc_dec_cnt < 0:
            if skip_diffs[bad_idxs[0]] >= -3 and skip_diffs[bad_idxs[0]] < 0:
                return True
    return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(prog='Day2', description='Python solution to Advent of Code Day 2 puzzle')
    utils.common_args(parser=parser)
    args = parser.parse_args()
  
    logger.debug(f"Opening {args.filename}")

    with open(args.filename, "r") as f:
        input = f.readlines()
    
    # safe_cnt = 0
    # for report in input:
    #     safe = True
    #     report = report.split()
    #     decreasing = False
    #     if int(report[0]) > int(report[1]):
    #         decreasing = True
    #     for i in range(len(report) - 1):
    #         if decreasing:
    #             if 0 < int(report[i]) - int(report [i+1]) < 4:
    #                 continue
    #             else:
    #                 safe = False
    #                 break
    #         if not decreasing:
    #             if 0 < int(report[i+1]) - int(report[i]) < 4:
    #                 continue
    #             else:
    #                 safe = False
    #                 break
    #     if safe:
    #         safe_cnt += 1
    # logger.info(safe_cnt)


    safe_cnt = 0
    for report in input:
        if run_report(report):
            safe_cnt +=1
    logger.info(safe_cnt)



# 1 3 2 4 5
# 2 -1 2 1
# 1 1 3 