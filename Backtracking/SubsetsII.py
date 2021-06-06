# [Leetcode 90](https://leetcode.com/problems/subsets-ii/)

from typing import List

class Solution:
    def __init__(self):
        self.ans = []

    def find(self, start, nums, comb):
        self.ans.append(comb[:])
        if len(comb) == len(nums):
            return

        for i in range(start, len(nums)):
            # Skip duplicated values (Note: the nums array has been sorted)
            if (i > start and nums[i] == nums[i-1]):
                continue
            comb.append(nums[i])
            self.find(i + 1, nums, comb)
            comb.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort() # It's necessary
        self.find(0, nums, [])
        return self.ans

s = Solution()
nums = [1,2,2]
print(s.subsetsWithDup(nums))
