"""solution.py"""

import math
import os
import random
import re
import sys

import time

def minimumBribes(q):
    """
    O(?)
    """
    len_q = len(q)
    total = 0
    for i, x in enumerate(q):
        if i < (len_q - 1) and q[i] > q[i+1]:
            q[i], q[i+1] = q[i+1], q[i]
            total += 1
            print(q)

    print('-->%s' % (total))
    return True


if __name__ == '__main__':
    input_path = 'input/'
    for filename in os.listdir(input_path):
        print('📂 %s' % (filename))
        f = open(input_path + filename, 'r')

        inputs = f.readlines()
        input_line = 0
        t = int(inputs[input_line])
        input_line += 1

        start_time = time.time()
        for t_itr in range(t):
            n = int(inputs[input_line])
            input_line += 1
            q = list(map(int, inputs[input_line].rstrip().split()))
            input_line += 1
            minimumBribes(q)
        print("⏰ %.12f seconds ⏰" % (time.time() - start_time))
