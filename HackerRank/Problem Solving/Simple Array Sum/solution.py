"""solution.py"""

import math
import os
import random
import re
import sys

import time
from pynput.keyboard import Key, Controller


def simpleArraySum(ar):
    """
    O(?)
    """
    return True


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
        simpleArraySum(arr)
        print("⏰ %.12f seconds ⏰" % (time.time() - start_time))
