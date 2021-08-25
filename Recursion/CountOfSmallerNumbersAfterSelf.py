from typing import List

# Merge Sort
class Solution:
    def __init__(self):
        self.ans = []

    def merge(self, left, right):
        i = j = 0
        tmp = []
        while i < len(left) and j < len(right):
            if left[i][1] < right[j][1]: 
                tmp.append(left[i])
                i+=1
            else: 
                tmp.append(right[j])
                j+=1

        while i < len(left): 
            tmp.append(left[i]) 
            i+=1

        while j < len(right): 
            tmp.append(right[j]) 
            j+=1

        return tmp

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])

        cnt = 0
        i, j = 0, 0
        while (i < len(left)):
            while j < len(right) and (right[j][1] < left[i][1]):
                j += 1
                cnt += 1
            self.ans[left[i][0]] += cnt
            i += 1

        return self.merge(left, right)

    def countSmaller(self, nums: List[int]) -> List[int]:
        self.ans = [0 for i in range(len(nums))]
        self.merge_sort(list(enumerate(nums)))
        return self.ans


# Using SortedList
from sortedcontainers import SortedList
class Solution2:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        bst = SortedList()
        ans = [0] * N
        for i in range(N-1, -1, -1):
            idx = bst.bisect_left(nums[i])
            ans[i] = idx
            bst.add(nums[i])
        return ans

s = Solution()
nums = [3,2,1,2]
print(s.countSmaller(nums))