# Monotonic Stack 原型

from typing import List
class Solution:
    def nextGreaterElement(self, nums):
        N = len(nums)
        stk = []
        ans = [-1] * N
        for i in range(N):
            n = nums[i]
            while stk and nums[stk[-1]] < n:
                ans[stk[-1]] = n
                stk.pop()
            stk.append(i)
        return ans        

s = Solution()
nums = [3, 5, 4, 6, 3, 4]
print(s.nextGreaterElement(nums))