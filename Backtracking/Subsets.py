# [Leetcode 78](https://leetcode.com/problems/subsets/)

from typing import List

class Solution:
    def __init__(self):
        self.ans = []

    def find(self, start, nums, comb):
        self.ans.append(comb[:])
        if len(comb) == len(nums):
            return

        for i in range(start, len(nums)):
            comb.append(nums[i])
            self.find(i + 1, nums,  comb)
            comb.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.find(0, nums, [])
        return self.ans

s = Solution()
nums = [1,2,3]
print(s.subsets(nums))
