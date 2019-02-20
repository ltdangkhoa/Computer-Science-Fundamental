"""solution.py"""

import math
import os
import random
import re
import sys

import timeit


def arrayManipulation(n, queries):
    """
    O(n)
    Up and Down, then sum and get highest peek
    """
    arr = [0]*(n+1)
    for x in queries:
        a = x[0]
        b = x[1]
        k = x[2]
        arr[a - 1] += k
        if b < n:
            arr[b] -= k

    max_value = sum_all = 0
    for i in arr:
        sum_all += i
        if max_value < sum_all:
            max_value = sum_all

    return max_value

def run_time_it():
    """Trigger timeit"""
    arrayManipulation(n, queries)

if __name__ == '__main__':
    INPUT_PATH = 'input/'
    for filename in os.listdir(INPUT_PATH):
        print('📂 %s' % (filename))
        f = open(INPUT_PATH + filename, 'r')

        inputs = f.readlines()
        input_line = 0
        nm = inputs[input_line].split()
        input_line += 1
        n = int(nm[0])
        m = int(nm[1])
        queries = []
        for _ in range(m):
            queries.append(list(map(int, inputs[input_line].rstrip().split())))
            input_line += 1

        print("⏰ %.12f seconds ⏰" % timeit.timeit(run_time_it, number=1))
