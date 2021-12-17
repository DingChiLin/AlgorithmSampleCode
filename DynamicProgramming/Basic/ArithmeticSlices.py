from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        DP = [0 for _ in range(N)]
        for i in range(2, N):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                DP[i] = DP[i-1] + 1
        return sum(DP)