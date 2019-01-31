"""solution.py"""

import math
import os
import random
import re
import sys

import time
from pynput.keyboard import Key, Controller


def diagonalDifference(arr):
    """
    Time O(n) Iterate only 1 time
    Space O(2n)
    """
    n = len(arr)
    l2r = []
    r2l = []
    for i in range(n):
        l2r.append(arr[i][i])
        r2l.append(arr[i][(n-1)-i])

    return abs(sum(l2r) - sum(r2l)) # T = 4


if __name__ == '__main__':
    input_path = 'input/'
    for filename in os.listdir(input_path):
        print('📂 %s' % (filename))
        f = open(input_path + filename, 'r')
        keyboard = Controller()
        keyboard.type(f.read())
        keyboard.press(Key.enter)

        n = int(input())
        arr = []
        for _ in range(n):
            arr.append(list(map(int, input().rstrip().split())))

        start_time = time.time()
        diagonalDifference(arr)
        print("⏰ %.12f seconds ⏰" % (time.time() - start_time))
