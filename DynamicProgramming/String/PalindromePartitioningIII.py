from math import inf
class Solution:
    def __init__(self):
        self.records = None # need to change k characters to make s in range [i,j] a palindrome

    def need_change_characters(self, s):
        self.records = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(0, j+1):
                if (s[i] == s[j]):
                    if (j - i < 2):
                        self.records[i][j] = 0
                    else:
                        self.records[i][j] = self.records[i+1][j-1]
                else:
                    self.records[i][j] = 1 + self.records[i+1][j-1]

    def palindromePartition(self, s: str, k: int) -> int:
        self.need_change_characters(s)
        dp = [[inf for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        dp[0][0] = 0
        for j in range(1, len(s)+1):
            for cut in range(1, j+1):
                for i in range(0, j):
                    dp[j][cut] = min(dp[j][cut], self.records[i+1-1][j-1] + dp[i][cut-1])

        return dp[len(s)][k]

s = Solution()
input = "aabbc"
k = 3
print(s.palindromePartition(input, k))