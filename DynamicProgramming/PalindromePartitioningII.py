from collections import defaultdict
from math import inf
class Solution:
    def __init__(self):
        self.records = None
        self.is_palindrome = None

    def find_palindrome(self, s):
        self.records = defaultdict(list)
        self.is_palindrome = [[False for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        for j in range(len(s)):
            for i in range(0, j+1):
                if (s[i] == s[j]) and ( j - i < 2 or self.is_palindrome[i+1][j-1]):
                    self.is_palindrome[i][j] = True
                    self.records[j].append(i)

    def minCut(self, s: str) -> int:
        self.find_palindrome(s)
        dp = [inf for i in range(len(s))]
        for j in range(len(s)):
            for i in self.records[j]:
                tmp = 1
                if (i > 0):
                    tmp += dp[i-1]
                dp[j] = min(dp[j], tmp)
        return dp[len(s)-1] - 1

s = Solution()
input = "aab"
print(s.minCut(input))
