from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        for i in range(1, N):
            if i <= dp[i-1]:
                dp[i] = max(dp[i-1], i + nums[i])
        if dp[N-1] >= N-1:
            return True
        else:
            return False