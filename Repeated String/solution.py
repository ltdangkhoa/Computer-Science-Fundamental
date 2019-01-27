"""solution.py"""

import math
import os
import random
import re
import sys

import time
from pynput.keyboard import Key, Controller


def repeatedString(s, n):
    """
    O(2n)
    The idea is to split repeated string into 2 part and sumup
    Count letter in single string and multiply repeate(floor of n/len(s)) times
    Count letter in spliced string (slice to modula of n%len(s))
    Count 2 times might reach O(n) + O(n)
    """
    char_to_count = 'a'
    single_len = len(s)
    single_count = s.count(char_to_count)  #O(n)
    repeat_count = math.floor(n / single_len)
    mod_a = n % single_len
    last_s = s[:mod_a]
    last_count = last_s.count(char_to_count)  #O(n)

    total_a = (single_count * repeat_count) + last_count

    return total_a


if __name__ == '__main__':
    input_path = 'input/'
    for filename in os.listdir(input_path):
        print('--->file %s' % (filename))
        f = open(input_path + filename, 'r')
        keyboard = Controller()
        keyboard.type(f.read())
        keyboard.press(Key.enter)
        s = input()
        n = int(input())
        start_time = time.time()
        repeatedString(s, n)
        print("--- %s seconds ---" % (time.time() - start_time))
