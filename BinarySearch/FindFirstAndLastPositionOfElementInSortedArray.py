from typing import List

class BinarySearch:
    def bisectLeft(self, nums, target):
        left = 0
        right = len(nums)
        while(left < right):
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left

    def bisectRight(self, nums, target):
        left = 0
        right = len(nums)
        while(left < right):
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        bs = BinarySearch()
        left = bs.bisectLeft(nums, target)
        if left == len(nums) or nums[left] != target: # can't find target in nums
            return [-1, -1]
        right = bs.bisectRight(nums, target)
        return [left, right - 1]

s = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(s.searchRange(nums, target))