"""solution.py"""

import math
import os
import random
import re
import sys

import timeit

def minimumSwaps(arr):
    """
    O(nlogn)
    """
    len_arr = len(arr)
    arr_dict = {key+1:value for key, value in enumerate(arr)}
    arr_checked = [False]*len_arr
    total_count = 0
    for key, value in arr_dict.items():
        count = 0

        while key != value and arr_checked[key-1] is False:
            arr_checked[value-1] = True
            count += 1
            value = arr_dict.get(value)

        arr_checked[key-1] = True
        total_count += count

    return total_count

def run_time_it():
    """Trigger timeit"""
    minimumSwaps(arr)

if __name__ == '__main__':
    INPUT_PATH = 'input/'
    for filename in os.listdir(INPUT_PATH):
        print('📂 %s' % (filename))
        f = open(INPUT_PATH + filename, 'r')

        inputs = f.readlines()
        input_line = 0
        n = int(inputs[input_line])
        input_line += 1
        arr = list(map(int, inputs[input_line].rstrip().split()))


        print("⏰ %.12f seconds ⏰" % timeit.timeit(run_time_it, number=1))
