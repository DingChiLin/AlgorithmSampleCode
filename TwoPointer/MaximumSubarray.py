from typing import List
from math import inf

# Find minimum position
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        curr = 0
        for n in nums:
            curr += n
            ans = max(ans, curr)
            if curr <= 0:
                curr = 0
        return ans

# Using prefix sum
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        preSum = [0] * (N+1)
        for i in range(N):
            preSum[i+1] = preSum[i] + nums[i]
        
        min_value = preSum[0]
        ans = -inf
        for i in range(1, N+1):
            ans = max(ans, preSum[i] - min_value)
            min_value = min(min_value, preSum[i])
        return ans