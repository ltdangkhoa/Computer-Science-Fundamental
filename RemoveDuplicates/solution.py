def removeDuplicates(nums, n):
    """
    :type nums: List[int]
    :rtype: int
    """
    new_id = 0
    for i in range(0, n - 1):
        if nums[i] != nums[i + 1]:
            nums[new_id] = nums[i]
            new_id += 1

    nums[new_id] = nums[n - 1]
    new_id += 1
    return new_id

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
n = len(nums)
n = removeDuplicates(nums, n)
for i in range(0, n):
    print(nums[i]);
