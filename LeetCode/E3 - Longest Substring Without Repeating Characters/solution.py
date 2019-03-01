"""solution.py"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count_dict = dict()
        longest_sub_str = 0
        repeat = False
        for x in s:
            ox = ord(x)
            if ox in count_dict:
                repeat = True
                len_sub = len(count_dict)
                if len_sub > longest_sub_str:
                    longest_sub_str = len_sub
                count_dict.clear()
            count_dict[ox] = 1


        longest_sub_str = longest_sub_str if repeat else len(s)

        print(longest_sub_str, '---')
        return longest_sub_str


solution = Solution()
solution.lengthOfLongestSubstring("abcabcbb")
solution.lengthOfLongestSubstring("au")
solution.lengthOfLongestSubstring(" ")
solution.lengthOfLongestSubstring("")
