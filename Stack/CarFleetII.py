from typing import List
from math import inf

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        stk = [] # [(position, velocity, time of collision)]
        N = len(cars)
        time = [inf for i in range(N)]
        for i in range(N-1, -1, -1):
            pos, v = cars[i]
            while stk and v <= cars[stk[-1]][1]:
                stk.pop()

            while stk and ((cars[stk[-1]][0] - pos) / (v - cars[stk[-1]][1])) >= time[stk[-1]]:
                stk.pop()

            if stk:
                time[i] = (cars[stk[-1]][0] - pos) / (v - cars[stk[-1]][1])
            stk.append(i) 

        return [(t if t != inf else -1) for t in time]

s = Solution()
cars = [[1,2],[2,1],[4,3],[7,2]]
cars = [[3,4],[5,4],[6,3],[9,1]]
print(s.getCollisionTimes(cars))