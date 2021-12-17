# [Leetcode 377](https://leetcode.com/problems/combination-sum-iv/)

from typing import List
from collections import defaultdict

# bottom-up
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for i in range(target+1):
            for n in nums:
                if (i >= n):
                    dp[i] += dp[i-n]
        return dp[target]

# top-down
class Solution2:
    def __init__(self):
        self.dp = []

    def helper(self, nums, remain):
        if self.dp[remain] != None:
            return self.dp[remain]

        if remain == 0:
            self.dp[remain] = 1
            return 1

        ans = 0
        for n in nums:
            if (remain >= n):
                ans += self.helper(nums, remain - n)
        self.dp[remain] = ans

        return ans

    def combinationSum4(self, nums: List[int], target: int) -> int: 
        self.dp = [None for i in range(target+1)]
        return self.helper(nums, target)

s = Solution()
nums = [1,2,3]
target = 4
print(s.combinationSum4(nums, target))
