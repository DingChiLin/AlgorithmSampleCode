from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot & 1: # odd number
            return False

        capacity = tot // 2

        N = len(nums)
        dp = [False for j in range(capacity + 1)]
        dp[0] = True
        for i in range(1, N + 1):
            for j in range(capacity, 0, -1):
                weight = nums[i-1]
                if (j - weight >= 0):
                    dp[j] |= dp[j - weight]
                else:
                    dp[j] = dp[j]
        return dp[capacity]

s = Solution()
nums = [1,5,11,5]
nums = [1,2,3,10]
print(s.canPartition(nums))