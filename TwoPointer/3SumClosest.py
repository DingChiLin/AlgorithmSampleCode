from typing import List
from math import inf

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        diff = inf
        for i in range(N-2):
            left = i + 1
            right = N - 1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if abs(target - val) < abs(diff):
                    diff = target - val
                if val > target:
                    right -= 1
                elif val < target:
                    left += 1
                else:
                    return target
        return target - diff
