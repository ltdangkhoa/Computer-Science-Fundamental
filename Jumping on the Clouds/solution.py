"""solution.py"""

import math
import os
import random
import re
import sys

import time
from pynput.keyboard import Key, Controller


def jumpingOnClouds(c):
    """
    Θ(log(n)) -> Θ(n): This approach won't traverse all items of the list
    It might pass by Cloud(1) or even double jump for Cloud(0)
    """
    current_cloud = 0
    total_jumps = 0
    lenc = len(c)
    while current_cloud != (lenc - 1):
        if current_cloud + 2 < lenc and c[current_cloud + 1] == 0 and c[current_cloud + 2] == 0:
            current_cloud += 2
        elif c[current_cloud + 1] == 1:
            current_cloud += 2
        else:
            current_cloud += 1

        total_jumps += 1
    return total_jumps


if __name__ == '__main__':
    input_path = 'input/'
    for filename in os.listdir(input_path):
        print('--->file %s' % (filename))
        f = open(input_path + filename, 'r')
        keyboard = Controller()
        keyboard.type(f.read())
        keyboard.press(Key.enter)
        n = int(input())
        c = list(map(int, input().rstrip().split()))
        start_time = time.time()
        jumpingOnClouds(c)
        print("--- %s seconds ---" % (time.time() - start_time))
