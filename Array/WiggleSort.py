from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        N = len(nums)
        for i in range(1, N):
            if i & 1:
                if nums[i] < nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
            else:
                if nums[i] > nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
