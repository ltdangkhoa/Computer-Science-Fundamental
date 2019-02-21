"""solution.py"""

import math
import os
import random
import re
import sys

import timeit

# from collections import Counter

def checkMagazine(magazine, note):
    """
    O(nk)
    To be improved: build a hash function to store keywords as numeric
    Much more simpler with built-in Python: using collections Counter
    """
    # print(Counter(magazine))
    # print(Counter(note))
    # c_note_magazie = len(Counter(note) - Counter(magazine))
    # print('Yes' if c_note_magazie == 0 else 'No')

    dict_magazine = {}
    for word in magazine:
        if not word in dict_magazine:
            dict_magazine[word] = 1
        else:
            dict_magazine[word] += 1

    can_replicate = True
    for word in note:
        if dict_magazine.get(word, 0) > 1:
            dict_magazine[word] -= 1
        elif dict_magazine.get(word, 0) == 1:
            dict_magazine.pop(word)
        else:
            can_replicate = False
            break

    print('Yes' if can_replicate else 'No')

def run_time_it():
    """Trigger timeit"""
    checkMagazine(magazine, note)

if __name__ == '__main__':
    INPUT_PATH = 'input/'
    for filename in os.listdir(INPUT_PATH):
        print('📂 %s' % (filename))
        f = open(INPUT_PATH + filename, 'r')

        inputs = f.readlines()
        input_line = 0
        mn = inputs[input_line].split()
        input_line += 1
        m = int(mn[0])
        n = int(mn[1])
        magazine = inputs[input_line].rstrip().split()
        input_line += 1
        note = inputs[input_line].rstrip().split()

        print("⏰ %.12f seconds ⏰" % timeit.timeit(run_time_it, number=1))
