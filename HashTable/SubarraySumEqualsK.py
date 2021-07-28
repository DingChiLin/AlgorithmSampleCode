from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        preSum = [0] * (N + 1)
        for i in range(N):
            preSum[i+1] = preSum[i] + nums[i]

        records = defaultdict(int)
        ans = 0
        for i in range(N+1):
            ans += records[preSum[i] - k]
            records[preSum[i]] += 1

        return None