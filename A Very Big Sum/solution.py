"""solution.py"""

import math
import os
import random
import re
import sys

import time
from pynput.keyboard import Key, Controller


def aVeryBigSum(ar):
    """
    O(?)
    """
    return sum(ar)


if __name__ == '__main__':
    input_path = 'input/'
    for filename in os.listdir(input_path):
        print('📂 %s' % (filename))
        f = open(input_path + filename, 'r')
        keyboard = Controller()
        keyboard.type(f.read())
        keyboard.press(Key.enter)

        ar_count = int(input())
        ar = list(map(int, input().rstrip().split()))

        start_time = time.time()
        aVeryBigSum(ar)
        print("⏰ %.12f seconds ⏰" % (time.time() - start_time))
