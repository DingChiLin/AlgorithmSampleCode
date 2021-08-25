from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        stk = [] # record end point
        for x, y in intervals:
            if stk and x < stk[-1]:
                continue
            stk.append(y)

        return len(intervals) - len(stk)

s = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(s.eraseOverlapIntervals(intervals))