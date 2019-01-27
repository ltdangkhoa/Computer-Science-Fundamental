#!/bin/python3

import math
import os
import random
import re
import sys

import time
from pynput.keyboard import Key, Controller

def countingValleys(n, s):
    """
    Time: O(n) - Travese through all elements on array
    Space: on-learning...
    """
    altitude = 0
    total_valley = 0
    is_in_valley = False
    for step in list(s):
        if step == 'U':
            altitude += 1
        else:
            altitude -= 1

        if altitude == -1:
            is_in_valley = True
        elif altitude == 0 and is_in_valley:
            is_in_valley = False
            total_valley += 1

    return total_valley

if __name__ == '__main__':
    input_path = 'input/'
    for filename in os.listdir(input_path):
        print('--->file %s' % (filename))
        f = open(input_path + filename, 'r')
        keyboard = Controller()
        keyboard.type(f.read())
        keyboard.press(Key.enter)
        n = int(input())
        s = input()
        start_time = time.time()
        countingValleys(n, s)
        print("--- %s seconds ---" % (time.time() - start_time))
