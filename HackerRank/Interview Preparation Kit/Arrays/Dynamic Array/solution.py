"""solution.py"""

import math
import os
import random
import re
import sys

import timeit

class SimpleXOR:
    def xor(self, a, b):
        return a ^ b

def dynamicArray(n, queries):
    last_answer = 0
    all_answer = []
    arr = [[] for _ in range(n)]
    xor = SimpleXOR()
    for row in queries:
        t = row[0]
        x = row[1]
        y = row[2]
        sn = xor.xor(x, last_answer) % n
        if t == 1:
            arr[sn].append(y)
        elif t == 2:
            last_answer = arr[sn][y%len(arr[sn])]
            all_answer.append(last_answer)

    return all_answer

def run_time_it():
    """Trigger timeit"""
    dynamicArray(n, queries)

if __name__ == '__main__':
    INPUT_PATH = 'input/'
    for filename in os.listdir(INPUT_PATH):
        print('📂 %s' % (filename))
        f = open(INPUT_PATH + filename, 'r')

        inputs = f.readlines()
        input_line = 0
        nq = inputs[input_line].rstrip().split()
        input_line += 1
        n = int(nq[0])
        q = int(nq[1])
        queries = []
        for _ in range(q):
            queries.append(list(map(int, inputs[input_line].rstrip().split())))
            input_line += 1

        print("⏰ %.12f seconds ⏰" % timeit.timeit(run_time_it, number=1))
