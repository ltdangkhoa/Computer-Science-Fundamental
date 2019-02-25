"""solution.py"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force
        T: O(n^2)
        S: O(1)
        """
        # i1 = 0
        # i2 = i1 + 1
        # len_nums = len(nums)
        # while nums[i1] + nums[i2] != target:
        #     if i2 < (len_nums - 1):
        #         i2 += 1
        #     else:
        #         i1 += 1
        #         i2 = i1 + 1
        #
        # return [i1, i2]

        """
        Two-pass hash table
        T: O(n)
        S: O(n)
        """
        # nums_min = {target - n: i for i,n in enumerate(nums)}
        # for i in range(len(nums)):
        #     if nums_min.get(nums[i]) and nums_min.get(nums[i]) != i:
        #         return [i, nums_min.get(nums[i])]

        """
        One-pass hash table
        T: O(n)
        S: O(n)
        """
        checked_dict = {}
        result = []
        for i, value in enumerate(nums):
            sub_value = target - value
            if value in checked_dict:
                result = [checked_dict[value], i]
                break
            else:
                checked_dict[sub_value] = i
        return result
