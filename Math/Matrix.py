class Matrix:
    def __init__(self, m):
        self.m = m

    # inplace rotate right (only for square matrix)
    def rotate(self):
        N = len(self.m[0])
        for i in range(N//2):
            for j in range((N+1)//2):
                self.m[j][N-1-i], self.m[N-1-i][N-1-j], self.m[N-1-j][i], self.m[i][j] = \
                self.m[i][j], self.m[j][N-1-i], self.m[N-1-i][N-1-j], self.m[N-1-j][i]

    # inplace transpose (only for square matrix)
    def transpose(self):
        N = len(self.m[0])
        for i in range(N):
            for j in range(i + 1, N):
                self.m[i][j], self.m[j][i] = self.m[j][i], self.m[i][j]
    
    # inplace reflect columns
    # [[1,2],  =>  [[2,1],
    #  [3,4]]       [4,3]]
    def reflect(self):
        N = len(self.m[0])
        for j in range(N // 2):
            for i in range(N):
                self.m[i][j], self.m[i][N-1-j] = self.m[i][N-1-j], self.m[i][j]

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

    def __eq__(self, B):
        N = len(self.m)
        M = len(self.m[0])
        if N != len(B.m) or M != len(B.m[0]):
            return False
        for i in range(N):
            for j in range(M):
                if self.m[i][j] != B.m[i][j]:
                    return False
        return True

    def __repr__(self):
        return repr(self.m)

m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[6, 5], [4, 3], [2, 1]])
print(m1.mult(m2))

m3 = Matrix([[10], [20], [30]])
print(m1.mult(m3))

m4 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m4)
m4.rotate()
print(m4)

m5 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m5.transpose()
print(m5)
m5.reflect()
print(m5)

print(m4 == m5)