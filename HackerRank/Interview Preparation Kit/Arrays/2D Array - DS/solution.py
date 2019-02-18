"""solution.py"""

import math
import os
import random
import re
import sys

import time
from pynput.keyboard import Key, Controller


def hourglassSum(arr):
    """
    O(n^2)
    """
    len_i = len(arr)
    len_j = len(arr[0])
    for i in range(len_i-2):
        for j in range(len_j-2):
            """
            Basic sum (faster than using sum(array))
            """
            sum_hg = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            sum_hg += arr[i+1][j+1]
            sum_hg += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            """
            Improve to use sum array
            """
            # top_sum = sum(arr[i][j:j+3])
            # mid_sum = arr[i+1][j+1]
            # bottom_sum = sum(arr[i+2][j:j+3])
            # sum_hg = top_sum + mid_sum + bottom_sum

            if i == 0 and j == 0:
                best_sum = sum_hg
            elif sum_hg > best_sum:
                best_sum = sum_hg

    return best_sum


if __name__ == '__main__':
    input_path = 'input/'
    for filename in os.listdir(input_path):
        print('📂 %s' % (filename))
        f = open(input_path + filename, 'r')
        keyboard = Controller()
        keyboard.type(f.read())
        keyboard.press(Key.enter)

        arr = []
        for _ in range(6):
            arr.append(list(map(int, input().rstrip().split())))

        start_time = time.time()
        result = hourglassSum(arr)
        print("⏰ %.12f seconds ⏰" % (time.time() - start_time))
