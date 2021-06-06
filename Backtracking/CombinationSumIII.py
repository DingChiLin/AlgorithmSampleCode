# [Leetcode 216](https://leetcode.com/problems/combination-sum-iii/)

from typing import List

class Solution:
    def __init__(self):
        self.ans = []

    def find(self, start, nums, max_length, target, comb):
        if target < 0: # pruning
            return

        if len(comb) == max_length: # search to the end
            if target == 0:
                self.ans.append(comb[:])
            return

        for i in range(start, len(nums)):
            comb.append(nums[i])
            self.find(i + 1, nums, max_length, target - nums[i], comb)
            comb.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        candidates = [i for i in range(1, 10)]
        self.find(0, candidates, k, n, [])
        return self.ans

s = Solution()
k = 3
n = 9
print(s.combinationSum3(k, n))
