from math import inf

class Solution:
    def floydWarshall(self, N, edges):
        dst = [[0 if i == j else inf for j in range(N)] for i in range(N)]
        for n1, n2, d in edges:
            dst[n1][n2] = d
            dst[n2][n1] = d

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if dst[i][j] > dst[i][k] + dst[k][j]:
                        dst[i][j] = dst[i][k] + dst[k][j]
        
        return dst


# direction: (bidirectional)
#        5    7
#     1 -- 3 -- 5
#   1/   2/ 1\ /3 
#  0 -- 2 -- 4
#     3    8
#

edges = {
    0: [(1,1), (2,3)],
    1: [(3,5)],
    2: [(3,2), (4,8)],
    3: [(4,1), (5,7)],
    4: [(5,3)],
    5: []
}

s = Solution()
edges = [
    [0, 1, 1], [0, 2, 3], [1, 3, 5],
    [2, 3, 2], [2, 4, 8], [3, 4, 1], 
    [3, 5, 7], [4, 5, 3]
]
print(s.floydWarshall(6, edges))