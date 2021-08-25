from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        ending = N-1
        for i in range(N-2, -1, -1):
            if nums[i] >= ending - i:
                ending = i

        return ending == 0

s = Solution()
nums = [2,3,1,1,4]
print(s.canJump(nums))