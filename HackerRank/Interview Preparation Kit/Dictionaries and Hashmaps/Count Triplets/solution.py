"""solution.py"""

import math
import os
import random
import re
import sys

import time

from collections import defaultdict

def countTriplets(arr, r):
    """
    O(?)
    """
    dict_2 = defaultdict(int)
    dict_3 = defaultdict(int)

    total_output = 0
    for value in arr:
        total_output += dict_3[value]
        dict_3[value*r] += dict_2[value]
        dict_2[value*r] += 1

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
