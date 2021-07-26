from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        left = 0
        right = (N + 1) // 2
        while(left < right):
            mid = (left + right) // 2
            index = mid * 2
            if (index < N-1) and (nums[index] == nums[index + 1]):
                left = mid + 1
            else:
                right = mid
        return nums[left * 2]

s = Solution()
nums = [0,1,1]
print(s.singleNonDuplicate(nums))
