from typing import List

class Solution:
    def __init__(self):
        self.ans = 0
    
    def find(self, left, right, nums, target):
        while left < right:
            if nums[left] + nums[right] > target:
                self.ans += (right - left)
                right -= 1
            else:
                left += 1
            
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        nums.sort()
        for i in range(2, len(nums)):
            self.find(0, i-1, nums, nums[i])
        return self.ans