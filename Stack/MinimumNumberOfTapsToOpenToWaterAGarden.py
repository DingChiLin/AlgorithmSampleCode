from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        stk = []
        for i in range(n+1):
            left = max(0, i - ranges[i])
            right = min(i + ranges[i], n)
            if stk and right <= stk[-1][1]:
                continue
            
            while stk and left <= stk[-1][0]:
                stk.pop()

            if stk:
                left = max(left, stk[-1][1])
            stk.append((left, right))

        if stk[0][0] != 0 or stk[-1][1] != n:
            return -1

        for i in range(len(stk)-1):
            if stk[i][1] < stk[i+1][0]:
                return -1

        return len(stk)

s = Solution()
n = 7
ranges = [1,2,1,0,2,1,0,1]

n = 8
ranges = [4,0,0,0,0,0,0,0,4]

n = 3
ranges = [0,0,0,0]

n = 9
ranges = [0,5,0,3,3,3,1,4,0,4]
print(s.minTaps(n, ranges))