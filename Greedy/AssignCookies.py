from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse = True)
        s.sort(reverse = True)
        ans = 0
        j = 0
        for i in range(len(s)):
            while j < len(g) and s[i] < g[j]:
                j += 1
            if j >= len(g):
                break
            ans += 1
            j += 1
        return ans

s = Solution()
g = [1,2,3]
ss = [1,1]
print(s.findContentChildren(g, ss))