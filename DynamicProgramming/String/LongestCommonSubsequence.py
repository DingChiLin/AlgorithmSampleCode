from functools import lru_cache

class Solution:
    def LCSMatrix(self, text1, text2):
        N = len(text1)
        M = len(text2)
        DP = [[0 for _ in range(M+1)] for _ in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, M+1):
                if (text1[i-1] == text2[j-1]):
                    DP[i][j] = DP[i-1][j-1] + 1
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])
        return DP

    def longestCommonSubsequence(self, text1: str, text2: str) -> int: 
        DP = self.LCSMatrix(text1, text2)
        return DP[-1][-1]
    
    def findAnyLCS(self, text1, text2):
        DP = self.LCSMatrix(text1, text2)
        N = len(text1)
        M = len(text2)
        i, j = N, M
        ans = ""
        while i > 0 and j > 0:
            if text1[i-1] == text2[j-1]:
                ans += text1[i-1]
                i -= 1
                j -= 1
            else:
                if DP[i-1][j] > DP[i][j-1]:
                    i -= 1
                else:
                    j -= 1
        
        return ans[::-1]

    @lru_cache(None)
    def findAllLCSHelper(self, id1, id2):
        if id1 == 0 or id2 == 0:
            return [""]

        res = []
        if self.text1[id1-1] == self.text2[id2-1]:
            t = self.text1[id1-1]
            candidates = self.findAllLCSHelper(id1-1, id2-1)
            for lcs in candidates:
                res.append(lcs + t)
            return res
        else:
            if self.DP[id1-1][id2] > self.DP[id1][id2-1]:
                return self.findAllLCSHelper(id1-1, id2)
            elif self.DP[id1-1][id2] < self.DP[id1][id2-1]:
                return self.findAllLCSHelper(id1, id2-1)
            else:
                candidates1 = self.findAllLCSHelper(id1-1, id2)
                candidates2 = self.findAllLCSHelper(id1, id2-1)
                return candidates1 + candidates2

    def findAllLCS(self, text1, text2):
        DP = self.LCSMatrix(text1, text2)
        N = len(text1)
        M = len(text2)
        self.text1 = text1
        self.text2 = text2
        self.DP = DP
        lcs = self.findAllLCSHelper(N, M)
        return sorted(list(set(lcs)))

S = Solution()
text1 = "abcdefg"
text2 = "xbdfgz"
print(S.longestCommonSubsequence(text1, text2))
print(S.findAnyLCS(text1, text2))
print(S.findAllLCS(text1, text2))

S = Solution()
text1 = "abcabcaa"
text2 = "acbacba"
print(S.longestCommonSubsequence(text1, text2))
print(S.findAnyLCS(text1, text2))
print(S.findAllLCS(text1, text2))
'''
ababa
abaca
abcba
acaba
acaca
acbaa
acbca
'''