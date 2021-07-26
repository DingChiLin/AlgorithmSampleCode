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

    def equal(self, m):
        N = len(self.m)
        M = len(self.m[0])
        if N != len(m) or M != len(m[0]):
            return False
        for i in range(N):
            for j in range(M):
                if self.m[i][j] != m[i][j]:
                    return False
        return True

m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[6, 5], [4, 3], [2, 1]])
print(m1.mult(m2))

m3 = Matrix([[10], [20], [30]])
print(m1.mult(m3))