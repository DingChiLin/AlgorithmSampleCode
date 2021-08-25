from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key = lambda p:p[0])
        count = 0
        start = points[0][0]
        end = points[0][1]

        for [s, e] in points:
            if s > end:
                count += 1
                end = e
            else:
                if e < end:
                    end = e

        return count + 1