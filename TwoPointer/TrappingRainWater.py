# [Leetcode 42](https://leetcode.com/problems/trapping-rain-water/)

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []
        ans = 0
        for i in range(len(height)):
            while(len(stk) > 0 and height[i] > height[stk[-1]]):
                if (len(stk) > 1):
                    w = i - stk[-2] - 1
                    h = min(height[i], height[stk[-2]]) - height[stk[-1]]
                    ans += w * h
                stk.pop()
            stk.append(i)

        return ans
