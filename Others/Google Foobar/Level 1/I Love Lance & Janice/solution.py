"""solution.py"""
from collections import defaultdict


def answer(s):  #pylint: disable=W,C
    """
    T: O(26 + N) = O(N)
    S: O(?)
    """
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    last_id = len(ascii_lowercase) - 1  #T: O(1) + O(1)
    encrypt_dict = defaultdict()
    for i, char in enumerate(ascii_lowercase):  #T: O(24)
        encrypt_dict[char] = ascii_lowercase[last_id - i]

    output = ""
    for char in s:  #T: O(N)
        output += encrypt_dict[char] if char in encrypt_dict else char

    return output


s = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"  #pylint: disable=W,C
result = "did you see last night's episode?"  #pylint: disable=W,C
assert answer(s) == result, "Error"

s = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"  #pylint: disable=W,C
result = "Yeah! I can't believe Lance lost his job at the colony!!"  #pylint: disable=W,C
assert answer(s) == result, "Error"
