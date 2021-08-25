from typing import List
from math import inf

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        i = 0
        tot = 0
        ans = inf
        for j in range(N):
            tot += nums[j]
            while i < j and tot - nums[i] >= target:
                tot -= nums[i]
                i += 1
            if tot >= target:
                ans = min(ans, (j - i + 1))
        return ans

s = Solution()
target = 7
nums = [2,3,1,2,4,3]
print(s.minSubArrayLen(target, nums))