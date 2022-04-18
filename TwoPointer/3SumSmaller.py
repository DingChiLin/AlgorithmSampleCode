from typing import List
from math import inf

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        ans = 0
        for i in range(N-2):
            left = i + 1
            right = N-1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val < target:
                    ans += (right - left)
                    left += 1
                else:
                    right -= 1
        return ans

S = Solution()
nums = [1,2,3,4,5,6,7,8]
target = 18
print(S.threeSumSmaller(nums, target)) # 49