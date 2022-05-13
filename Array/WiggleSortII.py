from typing import List
import random

# O(N) time
# O(N) space: only for reindex
class Solution:

    def find_median(self, nums):
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

        k = len(nums) // 2
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

    def partition(self, nums, target):
        pivot = target
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

    def new_index(self, index, N):
        middle = (N - 1) // 2
        if index <= middle:
            return (middle - index) * 2
        else:
            return 1 + (N - 1 - index) * 2

    def wiggleSort(self, nums: List[int]) -> None:
        N = len(nums)
        median = self.find_median(nums)
        self.partition(nums, median)
        new_nums = [0] * N
        for i in range(N):
            new_nums[self.new_index(i, N)] = nums[i]
        for i in range(N):
            nums[i] = new_nums[i]
        return nums