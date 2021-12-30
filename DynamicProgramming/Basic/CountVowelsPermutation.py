# Basic
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        DP = [[0 for _ in range(5)] for _ in range(n)]
        MOD = int(1e9) + 7
        DP[0] = [1,1,1,1,1] # initial
        
        # (a,e,i,o,u) => (0,1,2,3,4)
        for i in range(1, n):
            DP[i][0] = DP[i-1][1] + DP[i-1][2] + DP[i-1][4] # a preceded by e, i and u
            DP[i][1] = DP[i-1][0] + DP[i-1][2] # e preceded by a and i
            DP[i][2] = DP[i-1][1] + DP[i-1][3] # i preceded by e and o
            DP[i][3] = DP[i-1][2] # o preceded by i
            DP[i][4] = DP[i-1][2] + DP[i-1][3] # u preceded by i and o
            
            for j in range(5):
                DP[i][j] %= MOD
            
        return sum(DP[n-1]) % MOD
    
    
# Markov Chain
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        DP = [[0 for _ in range(5)] for _ in range(n)]
        MOD = int(1e9) + 7
        DP[0] = [1,1,1,1,1] # initial

        # (a,e,i,o,u) => (0,1,2,3,4)
        M = [
            [0,1,1,0,1],
            [1,0,1,0,0],
            [0,1,0,1,0],
            [0,0,1,0,0],
            [0,0,1,1,0]
        ]
        for i in range(1, n):  
            for j in range(5):
                for k in range(5):
                    DP[i][j] += DP[i-1][k] * M[j][k]
                DP[i][j] %= MOD
            
        return sum(DP[n-1]) % MOD

# O(1) space
class Solution:
    def countVowelPermutation(self, n: int) -> int: 
        a, e, i, o, u = 1, 1, 1, 1, 1
        MOD = int(1e9) + 7
        for _ in range(1, n):
            a, e, i, o, u =\
                (e + i + u) % MOD, (a + i) % MOD, (e + o) % MOD, i % MOD,  (i + o) % MOD
        return sum((a, e, i, o, u)) % MOD
        
        