"""solution.py"""

import math
import os
import random
import re
import sys

import time


def seqsum(n):
    return int((n**2 + n) / 2)

def hash_s(_s):
    """
    Hash and sum each charater from string
    """
    s_hashed = 0
    for _char in _s:
        s_hashed += hash(_char)
    return s_hashed

def sherlockAndAnagrams(s):
    """
    O(?)
    """
    count_dict = {}

    len_s = len(s)
    for i in range(len_s - 1):
        count_char = i + 1
        for j in range(len_s - i):
            s_spliced = s[j:j+count_char]
            s_hashed = hash_s(s_spliced)
            if count_dict.get(s_hashed):
                n_count = count_dict[s_hashed][0] + 1
                count_dict[s_hashed] = [n_count, seqsum(n_count - 1)]
            else:
                count_dict[s_hashed] = [1, 0]

    total_count = 0
    for key, value in count_dict.items():
        del key # Unused variable
        total_count += value[1]

    return total_count

    """
    O(?)
    """
    # from collections import Counter
    # from itertools import combinations
    #
    # count = []
    # for i in range(1, len(s) + 1):
    #     a = ["".join(sorted(s[j:j + i])) for j in range(len(s) - i + 1)]
    #     b = Counter(a)
    #     count.append(
    #         sum([len(list(combinations(['a'] * b[j], 2))) for j in b]))
    #
    # return sum(count)


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
            s = inputs[input_line]
            input_line += 1
            result = sherlockAndAnagrams(s)

        print("⏰ %.12f seconds ⏰" % (time.time() - start))
