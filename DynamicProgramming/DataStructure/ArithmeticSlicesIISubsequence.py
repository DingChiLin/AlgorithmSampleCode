from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        DP = defaultdict(int)
        for i in range(1, N):
            for j in range(0, i):
                diff = nums[i] - nums[j]
                DP[(i, diff)] += (1 + DP[(j, diff)])
        ans = sum(DP.values())
        return ans - ((N-1) * N // 2)
        
                