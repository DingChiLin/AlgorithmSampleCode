from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid < len(nums) - 1 and nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        return left