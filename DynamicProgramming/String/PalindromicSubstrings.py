class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        DP = [[False for _ in range(N)] for _ in range(N)]
        for i in range(N):
            DP[i][i] = True

        for i in range(N-2, -1, -1):
            for j in range(i+1, N):
                if s[i] == s[j] and (j == i+1 or DP[i+1][j-1]):
                    DP[i][j] = True
            
        # count "true" in DP matrix
        ans = 0
        for i in range(N):
            for j in range(N):
                if DP[i][j]:
                    ans += 1
        return ans


s = Solution()
ss = "aabaa"
print(s.countSubstrings(ss))