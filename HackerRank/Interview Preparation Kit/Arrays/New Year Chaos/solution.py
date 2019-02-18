"""solution.py"""

import math
import os
import random
import re
import sys

import time

def minimumBribes(q):
    """
    O(n)
    """
    step = 0
    len_q = len(q)
    for i in range(len_q, 0, -1):
        if q[i-1] == i:
            step += 0
        elif q[i-2] == i and i > 1:
            step += 1
            q[i-2], q[i-1] = q[i-1], q[i-2]
        elif q[i-3] == i and i > 2:
            step += 2
            q[i-3], q[i-2] = q[i-2], q[i-3]
            q[i-2], q[i-1] = q[i-1], q[i-2]
        else:
            step = False
            break

    print('Too chaotic' if step is False else step)


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
