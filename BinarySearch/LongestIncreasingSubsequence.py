from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        for n in nums:
            idx = bisect.bisect_left(ans, n)
            if idx == len(ans):
                ans.append(n)
            else:
                ans[idx] = n
        return len(ans)

s = Solution()
nums = []#[10,9,2,5,3,7,101,18]
print(s.lengthOfLIS(nums))
