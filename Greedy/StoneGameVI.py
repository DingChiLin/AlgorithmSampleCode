from typing import List
from math import inf, sqrt
from itertools import accumulate

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        values = list(zip(aliceValues, bobValues))
        values.sort(key = lambda x: x[0] + x[1])
        N = len(values)
        A = 0
        B = 0
        for i in range(N):
            if i & 1:
                B += values[N-1-i][1]
            else:
                A += values[N-1-i][0]
        if A > B:
            return 1
        elif A < B:
            return -1
        else:
            return 0

s = Solution()
aliceValues = [2,4,3]
bobValues = [1,6,7]

# aliceValues = [1,2]
# bobValues = [3,1]

aliceValues = [1,3]
bobValues = [2,1]
print(s.stoneGameVI(aliceValues, bobValues))