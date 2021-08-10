from typing import List

# order by right bar
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[1])
        stk = []
        for l, r in intervals:
            while stk and l <= stk[-1][1]:
                l = min(l, stk[-1][0])
                stk.pop()
            stk.append([l, r])
        return stk

# order by left bar
class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stk = []
        for l, r in intervals:
            if not stk:
                stk.append([l, r])
            else:
                if l > stk[-1][1]:
                    stk.append([l, r])
                else:
                    if r > stk[-1][1]:
                        stk[-1][1] = r

        return stk


s = Solution2()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(s.merge(intervals))