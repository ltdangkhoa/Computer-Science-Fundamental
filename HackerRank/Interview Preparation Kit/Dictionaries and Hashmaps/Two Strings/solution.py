"""solution.py"""

import math
import os
import random
import re
import sys

import time


def twoStrings(s1, s2):
    """
    O(?)
    Difference s2-s1: O(len(s2))
    """
    my_set_1 = set(s1)
    my_set_2 = set(s2)
    my_sub_set = my_set_2 - my_set_1

    return 'NO' if my_sub_set == my_set_2 else 'YES'


if __name__ == '__main__':
    INPUT_PATH = 'input/'
    for filename in os.listdir(INPUT_PATH):
        print('📂 %s' % (filename))
        f = open(INPUT_PATH + filename, 'r')

        inputs = f.readlines()
        input_line = 0

        q = int(inputs[input_line])
        input_line += 1

        start = time.time()

        for q_itr in range(q):
            s1 = inputs[input_line]
            input_line += 1
            s2 = inputs[input_line]
            input_line += 1
            twoStrings(s1, s2)

        print("⏰ %.12f seconds ⏰" % (time.time() - start))
