from typing import List
from math import inf

class Solution:
    def floydWarshall(self, N, edges):
        dst = [[0 if i == j else inf for j in range(N)] for i in range(N)]
        for n1, n2, d in edges:
            dst[n1][n2] = d

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if dst[i][j] > dst[i][k] + dst[k][j]:
                        dst[i][j] = dst[i][k] + dst[k][j]
        
        return dst

    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edges = [[pre, course, 1] for pre, course in prerequisites]
        dst = self.floydWarshall(n, edges)
        return [(dst[u][v] != inf) for u, v in queries]

s = Solution()
numCourses = 3
prerequisites = [[1,2],[1,0],[2,0]]
queries = [[1,0],[1,2]]
print(s.checkIfPrerequisite(numCourses, prerequisites, queries))
