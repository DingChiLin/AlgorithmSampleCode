from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, left_index, right_index):
            # randomized choose pivot position
            pivot_index = random.randint(left_index, right_index-1)
            nums[pivot_index], nums[right_index - 1] = nums[right_index - 1], nums[pivot_index]
           
            # swap values
            pivot = nums[right_index - 1]
            i = left_index
            for j in range(left_index, right_index - 1):
                if (nums[j] < pivot):
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right_index-1] = nums[right_index-1], nums[i]
            return i

        k = len(nums) - k
        lo = 0
        hi = len(nums)
        pivot = -1
        
        while pivot != k:
            pivot = partition(nums, lo, hi)
            if pivot < k:
                lo = pivot + 1
                hi = hi
            elif pivot > k:
                lo = lo
                hi = pivot

        return nums[pivot]

s = Solution()
nums = [3,2,1,5,6,4]
k = 2

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(s.findKthLargest(nums, k))