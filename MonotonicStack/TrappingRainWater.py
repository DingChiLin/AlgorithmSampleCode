from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []
        ans = 0
        for i in range(len(height)):
            while stk and height[i] > height[stk[-1]]:
                if (len(stk) > 1):
                    w = i - stk[-2] - 1
                    h = min(height[i], height[stk[-2]]) - height[stk[-1]]
                    ans += w * h
                stk.pop()
            stk.append(i)

        return ans

s = Solution()
height = [4,2,0,3,2,5]
print(s.trap(height))