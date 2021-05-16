# [Leetcode 77](https://leetcode.com/problems/combinations/)

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def helper(index, length, comb):
            # already have k elements in this combination
            if length == k:
                ans.append(comb[:])
                return

            # index should be 1 ~ n
            if (index > n):
                return

            # use this index
            comb.append(index)
            helper(index + 1, length + 1, comb)
            comb.pop()

            # not use this index
            helper(index + 1, length, comb)

        helper(1, 0, [])
        return ans

    def combine2(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def helper(start_index, length, comb):
            # already have k elements in this combination
            if length == k:
                ans.append(comb[:])
                return

            for i in range(start_index, n+1):
                comb.append(i)
                helper(i + 1, length + 1, comb)
                comb.pop()

        helper(1, 0, [])
        return ans


s = Solution()
n = 4
k = 3
print(s.combine(n, k))
print(s.combine2(n, k))