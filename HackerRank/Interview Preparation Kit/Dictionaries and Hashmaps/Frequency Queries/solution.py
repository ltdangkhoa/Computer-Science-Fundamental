"""solution.py"""

import math
import os
import random
import re
import sys

import time

from collections import defaultdict


def freqQuery(queries):
    """
    O(?)
    """
    # print(queries)
    elementFreq = defaultdict(int)
    freqCount = defaultdict(int)
    ans = []
    for i, j in queries:
        if i == 1:
            if freqCount[elementFreq[j]]:
                freqCount[elementFreq[j]] -= 1
            elementFreq[j] += 1
            freqCount[elementFreq[j]] += 1
        elif i == 2:
            if elementFreq[j]:
                freqCount[elementFreq[j]] -= 1
                elementFreq[j] -= 1
                freqCount[elementFreq[j]] += 1
        else:
            ans.append(1 if j in freqCount and freqCount[j] else 0)

        print(i, j, elementFreq, freqCount, ans)
    return ans


if __name__ == '__main__':
    INPUT_PATH = 'input/'
    for filename in os.listdir(INPUT_PATH):
        print('📂 %s' % (filename))
        f = open(INPUT_PATH + filename, 'r')

        inputs = f.readlines()
        input_line = 0

        q = int(inputs[input_line].strip())
        input_line += 1
        queries = []
        for _ in range(q):
            queries.append(list(map(int, inputs[input_line].rstrip().split())))
            input_line += 1

        start = time.time()
        ans = freqQuery(queries)
        print("⏰ %.12f seconds ⏰" % (time.time() - start))
