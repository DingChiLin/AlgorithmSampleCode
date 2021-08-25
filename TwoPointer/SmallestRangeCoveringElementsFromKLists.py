from typing import List
from math import inf
from collections import Counter

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        A = []
        for i, arr in enumerate(nums):
            for n in arr:
                A.append((n, i))
        A.sort()

        N = len(A)
        K = len(nums)
        interval = [-inf, inf]
        i = 0
        records = Counter()
        for j in range(N):
            records[A[j][1]] += 1
            while len(records) == K:
                x, y = A[i][0], A[j][0]
                if (y - x) < interval[1] - interval[0]:
                    interval = [x, y]
                records[A[i][1]] -= 1
                if records[A[i][1]] == 0:
                    del records[A[i][1]]
                i += 1
        return interval


s = Solution()
nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
nums = [[1],[2],[3],[4],[5],[6],[7]]
print(s.smallestRange(nums))