from typing import List
from math import inf

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ans = inf
        records = set()
        for x1, y1 in points:
            for x2, y2 in records:
                if (x2, y1) in records and (x1, y2) in records:
                    ans = min(ans, abs(x2 - x1) * abs(y2 - y1))
            records.add((x1, y1))
        return ans if ans != inf else 0

s = Solution()
points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
print(s.minAreaRect(points))