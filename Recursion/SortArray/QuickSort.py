# [Leetcode 912](https://leetcode.com/problems/sort-an-array/)

import random
class Solution:
    def partition(self, nums, left_index, right_index):
        # randomized choose pivot position
        pivot_index = random.randint(left_index, right_index-1)
        nums[pivot_index], nums[right_index - 1] = nums[right_index - 1], nums[pivot_index]

        # partition
        pivot = nums[right_index - 1]
        i = left_index
        for j in range(left_index, right_index - 1):
            if (nums[j] < pivot):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right_index-1] = nums[right_index-1], nums[i]
        return i

    def quick_sort_helper(self, nums, left_index, right_index):
        if (left_index >= right_index):
            return
        mid = self.partition(nums, left_index, right_index)
        self.quick_sort_helper(nums, left_index, mid)
        self.quick_sort_helper(nums, mid + 1, right_index)

    def sortArray(self, nums):
        self.quick_sort_helper(nums, 0, len(nums))
        return nums

s = Solution()
nums = [1,8,4,7,9,3,6,2,5]
nums = [2,1,2,1,3,1,3,2,1]
print(s.sortArray(nums))

# since it's an in-place sort, the original array will be changed
print(nums)