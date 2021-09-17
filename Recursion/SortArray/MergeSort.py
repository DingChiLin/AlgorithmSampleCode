# [Leetcode 912](https://leetcode.com/problems/sort-an-array/)

class Solution:
    def merge(self, left, right):
        i = j = 0
        tmp = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]: 
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

    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)

s = Solution()
nums = [1,8,4,7,5,3,6,2]
print(s.sortArray(nums))