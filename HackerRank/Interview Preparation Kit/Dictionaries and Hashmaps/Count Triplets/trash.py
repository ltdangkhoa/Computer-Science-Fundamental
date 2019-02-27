"""solution.py"""

import math
import os
import random
import re
import sys

import time

def countTriplets(arr, r):
    """
    O(?)
    """
    # print(arr, r)
    # print(nCr(4,3))
    # arr_dict = {}
    # for x in arr:
    #     if x in arr_dict:
    #         arr_dict[x] += 1
    #     else:
    #         arr_dict[x] = 1
    #
    # print(arr_dict)
    #
    # # arr_counted = [(k, v) for k, v in arr_dict.items()]
    # # arr_counted = sorted([(k, v) for k, v in arr_dict.items()], key=lambda tup: tup[0])
    # # arr_counted = sorted(arr_counted, key=lambda tup: tup[0])
    # # print(arr_counted)
    #
    # total_output = 0
    # # for i in range(len(arr_counted) - 2):
    # #     if (arr_counted[i][0] * r == arr_counted[i+1][0]
    # #             and arr_counted[i+1][0] * r == arr_counted[i+2][0]):
    # #         total_output += arr_counted[i][1]*arr_counted[i+1][1]*arr_counted[i+2][1]
    #
    # for key, value in arr_dict.items():
    #     if arr_dict.get(key*r) and arr_dict.get(key*r*r):
    #         sum_times = arr_dict[key] + arr_dict[key*r] + arr_dict[key*r*r]
    #         print(key, key*r, key*r*r, '->', arr_dict[key], arr_dict[key*r], arr_dict[key*r*r], '->', sum_times)
    #         if r == 1:
    #             total_output += nCr(arr_dict[key], 3)
    #         else:
    #             total_output += arr_dict[key]*arr_dict[key*r]*arr_dict[key*r*r]

    # print(total_output)

    return total_output


if __name__ == '__main__':
    INPUT_PATH = 'input/'
    for filename in os.listdir(INPUT_PATH):
        print('📂 %s' % (filename))
        f = open(INPUT_PATH + filename, 'r')

        inputs = f.readlines()
        input_line = 0

        nr = inputs[input_line].rstrip().split()
        input_line += 1
        n = int(nr[0])
        r = int(nr[1])
        arr = list(map(int, inputs[input_line].rstrip().split()))

        start = time.time()
        ans = countTriplets(arr, r)
        print("⏰ %.12f seconds ⏰" % (time.time() - start))
