from math import inf
from collections import defaultdict
class Solution:
    def __init__(self):
        self.records = None # 1 based
        self.is_palindrome = None # 0 based

    def find_palindrome(self, s):
        self.records = defaultdict(list)
        self.is_palindrome = [[False for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        for j in range(len(s)):
            for i in range(0, j+1):
                if (s[i] == s[j]) and ( j - i < 2 or self.is_palindrome[i+1][j-1]):
                    self.is_palindrome[i][j] = True
                    self.records[j+1].append(i+1)

    def checkPartitioning(self, s: str) -> bool:
        self.find_palindrome(s)
        dp = [[False for _ in range(4)] for _ in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1, len(s)+1):
            for k in range(1, 4):
                for i in self.records[j]:
                    dp[j][k] = dp[j][k] or dp[i-1][k-1]
        return dp[len(s)][3]

s = Solution()
input = "bbab"
print(s.checkPartitioning(input))