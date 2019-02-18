"""solution.py"""

import math
import os
import random
import re
import sys

import time
from pynput.keyboard import Key, Controller


def plusMinus(arr):
    """
    O(n)
    """

    def splitFunc(arr, brr):
        if len(arr) > 1:
            mid_index = len(arr) // 2
            leftarr = arr[:mid_index]
            rightarr = arr[mid_index:]

            splitFunc(leftarr, brr)
            splitFunc(rightarr, brr)
        else:
            if arr[0] < 0:
                brr[0] += 1
            elif arr[0] == 0:
                brr[1] += 1
            else:
                brr[2] += 1

    def iterateFunc(arr, brr):
        for x in arr:
            if x < 0:
                brr[0] += 1
            elif x == 0:
                brr[1] += 1
            else:
                brr[2] += 1

        return brr

    brr = [0, 0, 0]
    # splitFunc(arr, brr)
    brr = iterateFunc(arr, brr)

    denominator = len(arr)

    print("%2.6f\n%2.6f\n%2.6f" % (brr[2] / denominator, brr[0] / denominator,
                                   brr[1] / denominator))


if __name__ == '__main__':
    input_path = 'input/'
    for filename in os.listdir(input_path):
        print('📂 %s' % (filename))
        f = open(input_path + filename, 'r')
        keyboard = Controller()
        keyboard.type(f.read())
        keyboard.press(Key.enter)

        n = int(input())
        arr = list(map(int, input().rstrip().split()))

        start_time = time.time()
        plusMinus(arr)
        print("⏰ %.12f seconds ⏰" % (time.time() - start_time))
