#!/bin/python3

import math
import os
import random
import re
import sys
import time

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
    f = open('input14.txt', 'r')
    fl = f.readlines()
    n = fl[0]
    s = fl[1]

    start_time = time.time()
    # assert countingValleys(n, s) == 1, "Wrong"
    assert countingValleys(n, s) == 718, "Wrong"
    print("--- %s seconds ---" % (time.time() - start_time))
