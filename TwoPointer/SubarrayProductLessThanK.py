from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        i = 0
        cur = 1
        ans = 0
        for j in range(N):
            cur *= nums[j]
            while i < j and cur >= k:
                cur /= nums[i]
                i += 1
            if cur < k:
                ans += (j - i + 1)
            
        return ans

s = Solution()
nums = [10,5,2,6]
k = 100
print(s.numSubarrayProductLessThanK(nums, k))