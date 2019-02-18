"""solution.py"""

import math
import os
import random
import re
import sys

import time
from pynput.keyboard import Key, Controller

class SimpleQueue:
    """
    SimpleQueue
    """
    def __init__(self, arr):
        self.items = arr

    def add_left(self, obj):
        """Insert at left"""
        self.items.insert(0, obj)

    def add_right(self, obj):
        """Insert at right"""
        self.items.append(obj)

    def remove_left(self):
        """Remove at left"""
        return self.items.pop(0)

    def remove_right(self):
        """Remove at right"""
        return self.items.pop()

    def show(self):
        """Return list of queue"""
        return self.items

def rotLeft(a, d):
    """
    Simple solution by slicing and concatenate array
    Fast
    """
    i = d%len(a)
    return a[i:] + a[:i]

    """
    Complicated solution with queue demonstration
    Slow
    """
    # queue = SimpleQueue(a)
    # len_a = len(a)
    # if d > len_a//2:
    #     for _ in range(len_a - d):
    #         queue.add_left(queue.remove_right())
    # else:
    #     for _ in range(d):
    #         queue.add_right(queue.remove_left())
    #
    # return queue.show()


if __name__ == '__main__':
    input_path = 'input/'
    for filename in os.listdir(input_path):
        print('📂 %s' % (filename))
        f = open(input_path + filename, 'r')

        inputs = f.readlines()
        input_line = 0

        nd = inputs[input_line].split()
        input_line += 1
        n = int(nd[0])
        d = int(nd[1])
        a = list(map(int, inputs[input_line].rstrip().split()))

        start_time = time.time()
        result = rotLeft(a, d)
        print("⏰ %.12f seconds ⏰" % (time.time() - start_time))
