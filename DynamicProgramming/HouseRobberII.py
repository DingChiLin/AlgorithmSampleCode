from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = 0

        # rob first house
        rob = nums[0]
        rest = 0
        for i in range(1, len(nums) - 1):
            rob, rest = nums[i] + rest, max(rob, rest)
        ans = max(ans, rob, rest)

        # don't rob first house
        rob = 0
        rest = 0
        for i in range(1, len(nums)):
            rob, rest = nums[i] + rest, max(rob, rest)
        ans = max(ans, rob, rest)

        return ans