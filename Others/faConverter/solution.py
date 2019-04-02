"""solution.py"""

import math
import os
import random
import re
import sys

import timeit


def faConverter(arr):
    """
    """
    # print(arr)
    results = []
    for _s in arr:
        converted = []
        converted.append('fa')
        go_up = True
        for _c in _s:
            if _c == '-':
                go_up = True
                continue
            if go_up:
                converted.append(_c.upper())
            else:
                converted.append(_c)
            go_up = False

        results.append(''.join(converted))

    return ', '.join(results)


if __name__ == '__main__':
    INPUT_PATH = 'input/'
    for filename in os.listdir(INPUT_PATH):
        print('📂 %s' % (filename))
        f = open(INPUT_PATH + filename, 'r')

        inputs = f.readlines()
        input_line = 0
        queries = []
        for _ in range(len(inputs)):
            s = inputs[input_line].rstrip()
            queries.append(s)
            input_line += 1

        fa_converted = faConverter(queries)
        print(fa_converted)
