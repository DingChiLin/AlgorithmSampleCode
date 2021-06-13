class Solution:
    def numTrees(self, n: int) -> int:
        s = [0 for i in range(n+1)]
        s[0] = s[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                s[i] += s[j] * s[i-j-1]
        return s[-1]