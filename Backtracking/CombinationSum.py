# [Leetcode 39](https://leetcode.com/problems/combination-sum/)

from typing import List

class Solution:
    def __init__(self):
        self.ans = []

    def find(self, start, nums, target, comb):
        if target == 0: # find an valid combination
            self.ans.append(comb[:])

        if target <= 0: # pruning
            return

        for i in range(start, len(nums)):
            comb.append(nums[i])
            self.find(i, nums, target - nums[i], comb)
            comb.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.find(0, candidates, target, [])
        return self.ans

s = Solution()
candidates = [2,3,5]
target = 8
print(s.combinationSum(candidates, target))
