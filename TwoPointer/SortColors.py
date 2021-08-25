from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        pivot = 1
        left = 0
        right = len(nums) - 1

        i = 0
        while i <= right:
            if nums[i] < pivot:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            elif nums[i] > pivot:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                i -= 1
            i += 1