# [Leetcode 912](https://leetcode.com/problems/sort-an-array/)

# 3-way partition
import random
class Solution:
    def three_way_partition(self, nums, left_index, right_index):
        # randomized choose pivot position
        pivot_index = random.randint(left_index, right_index-1)
        nums[pivot_index], nums[right_index - 1] = nums[right_index - 1], nums[pivot_index]

        # 3 way partition
        pivot = nums[right_index - 1]
        lt = left_index
        gt = right_index - 1
        i = left_index
        while i <= gt:
            if nums[i] < pivot:
                nums[i], nums[lt] = nums[lt], nums[i]
                lt += 1
            elif nums[i] > pivot:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
                i -= 1
            i += 1
        return lt, gt

    def quick_sort_helper(self, nums, left_index, right_index):
        if (left_index >= right_index):
            return
        mid1, mid2 = self.three_way_partition(nums, left_index, right_index)
        self.quick_sort_helper(nums, left_index, mid1)
        self.quick_sort_helper(nums, mid2 + 1, right_index)

    def sortArray(self, nums):
        self.quick_sort_helper(nums, 0, len(nums))
        return nums

s = Solution()
nums = [1,8,4,7,9,3,6,2,5]
nums = [2,1,2,1,3,1,3,2,1]
print(s.sortArray(nums))

# since it's an in-place sort, the original array will be changed
print(nums)