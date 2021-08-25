from typing import List
from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        records = defaultdict(int)
        cnt = 0
        for n in nums:
            if n in records:
                cnt += records[n]
            records[n] += 1
        return cnt

s = Solution()
nums = [1,2,3,1,1,3]
print(s.numIdenticalPairs(nums))