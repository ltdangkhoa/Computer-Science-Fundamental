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
    count = 0
    len_arr = len(arr)
    arr_dict = {}

    for i, item in enumerate(arr):
        # arr_dict[item-1] = i
        arr_dict[item] = i+1

    checked = [False]*len_arr
    vis = {k:False for k in range(n)}

    print(vis)
    print(arr_dict)
    print(sorted(arr_dict.items(), key=lambda x: x[0]))

    for key, value in sorted(arr_dict.items(), key=lambda x: x[0]):
        print('k', key, 'v', value, checked[key-1])
        if checked[key-1] or key == value:
            continue

        c_c = 0
        value = key
        while not checked[value-1]:
            print('--', key, value, arr_dict[value], checked[value-1])
            checked[value-1] = True
            value = arr_dict[value]
            c_c += 1

        count += c_c - 1

    print(count)
    return count

    # len_arr = len(arr)
    # i = 0
    # count = 0
    # while i < len_arr:
    #     for j in range(i, len_arr):
    #         if arr[j] == i+1:
    #             if i != j:
    #                 arr[j], arr[i] = arr[i], arr[j]
    #                 count += 1
    #             break
    #     i += 1
    #
    # return count

    # n = len(arr)
    # arrpos = [*enumerate(arr)]
    #
    # arrpos.sort(key = lambda it:it[1])
    # vis = {k:False for k in range(n)}
    #
    # ans = 0
    # for i in range(n):
    #     if vis[i] or arrpos[i][0] == i:
    #         continue
    #
    #     cycle_size = 0
    #     j = i
    #     while not vis[j]:
    #         vis[j] = True
    #         j = arrpos[j][0]
    #         cycle_size += 1
    #
    #     if cycle_size > 0:
    #         ans += (cycle_size - 1)
    # return ans

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
