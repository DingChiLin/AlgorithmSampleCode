from typing import List
from math import inf

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)
        stk = []
        middle = -inf
        for i in range(N-1, -1, -1):
            n = nums[i]
            if n < middle:
                return True
            while stk and n > stk[-1]:
                middle = stk.pop()
            stk.append(n)
        return False