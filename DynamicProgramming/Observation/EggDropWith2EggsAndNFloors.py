'''
DP: https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/discuss/1248069/Recursive-Iterative-Generic
Math: https://www.itread01.com/content/1542577462.html
'''


'''
Naive DP
'''
from cmath import inf
from functools import lru_cache

'''
dp[n]: The time we need to test for n floor using two eggs
Time: O(N^2)
'''
class Solution:
    @lru_cache(None)
    def dp(self, n):
        if n == 0:
            return 0
        res = inf
        for i in range(1, n+1):
            res = min(res, 1 + max(i-1, self.dp(n-i)))
        return res

    def twoEggDrop(self, n: int) -> int:
        return self.dp(n)

'''
dp[k]: The floor we can test for dropping two eggs k times
dp[k] = sum(
    1: test this time 
    dp[k-1]: if not broke, we still have 2 eggs and k-1 times
    i-1: if broke, we still have 1 eggs and k-1 times
)
Either way, we can find the position of break for floor which have dp[k] floors using only k times of test

Time: O(N)
'''
class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i] = 1 + dp[i - 1] + i - 1
            if dp[i] >= n:
                return i

S = Solution()
n = 100
print(S.twoEggDrop(n))