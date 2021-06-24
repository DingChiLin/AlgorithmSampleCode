from typing import List

# 2 * 1D Array
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = [0 for _ in range(len(nums))]
        rest = [0 for _ in range(len(nums))]
        rob[0] = nums[0]
        rest[0] = 0
        for i in range(1, len(nums)):
            rob[i] = nums[i] + rest[i-1]
            rest[i] = max(rob[i-1], rest[i-1])
        return max(rob[-1], rest[-1])

# No Array
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = nums[0]
        rest = 0
        for i in range(1, len(nums)):
            rob, rest = nums[i] + rest, max(rob, rest)
        return max(rob, rest)

s = Solution()
nums = [2,7,9,3,1]
nums = [1,2,3,1]
print(s.rob(nums))