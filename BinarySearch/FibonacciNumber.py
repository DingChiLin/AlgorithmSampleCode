class Matrix:
    def __init__(self, m):
        self.m = m

    def mult(self, B):
        N = len(self.m)
        M = len(self.m[0])    
        R = len(B.m[0])
        ans = Matrix([[0 for _ in range(R)] for _ in range(N)])
        for i in range(N):
            for j in range(R):
                for k in range(M):
                    ans.m[i][j] += self.m[i][k] * B.m[k][j]
        return ans

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
 
        n -= 1
        ans = Matrix([[1], [0]])
        cur = Matrix([[1, 1], [1, 0]])
        while(n > 0):
            if (n & 1):
                ans = cur.mult(ans)
            cur = cur.mult(cur)
            n >>= 1

        return ans.m[0][0]

s = Solution()
n = 10
print(s.fib(n))
