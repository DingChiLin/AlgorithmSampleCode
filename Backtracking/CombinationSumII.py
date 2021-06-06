# [Leetcode 40](https://leetcode.com/problems/combination-sum-ii/)

from typing import List

class Solution:
    def __init__(self):
        self.ans = []

    def find(self, start, nums, target, comb):
        if target == 0: # find an valid combination
            self.ans.append(comb[:])

        if target <= 0: # pruning
            return

        if len(comb) == len(nums): # search to the end
            return

        for i in range(start, len(nums)):
            if (i > start and nums[i] == nums[i-1]):
                continue
            comb.append(nums[i])
            self.find(i + 1, nums, target - nums[i], comb)
            comb.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        self.find(0, candidates, target, [])
        return self.ans

s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(s.combinationSum2(candidates, target))
