from typing import List

class UnionFind:
    def __init__(self, N):
        self.nodes = [i for i in range(N)]
        self.rank = [1 for i in range(N)]       

    def root(self, n):
        if n != self.nodes[n]:
            self.nodes[n] = self.root(self.nodes[n])
        return self.nodes[n]

    def union(self, n1, n2):
        r1 = self.root(n1)
        r2 = self.root(n2)
        if r1 != r2:
            if self.rank[r1] < self.rank[r2]:
                self.nodes[r1] = r2
            elif self.rank[r1] > self.rank[r2]:
                self.nodes[r2] = r1
            else:
                self.nodes[r2] = r1
                self.rank[r1] += 1

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        N = len(heights)
        M = len(heights[0])
        if (N == 1 and M == 1):
            return 0

        dst = []
        for x in range(N):
            for y in range(M):
                if x < N-1:
                    nx = x + 1
                    ny = y
                    d = abs(heights[nx][ny] - heights[x][y])
                    dst.append((d, x * M + y, nx * M + ny))
                if y < M-1:
                    nx = x
                    ny = y + 1
                    d = abs(heights[nx][ny] - heights[x][y])
                    dst.append((d, x * M + y, nx * M + ny))

        dst.sort()
        u = UnionFind(N * M)
        start = 0
        end = N * M - 1
        for (d, n1, n2) in dst:
            u.union(n1, n2)
            if u.root(start) == u.root(end):
                return d

s = Solution()
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
heights = [[1,2,2],[3,8,2],[5,3,5]]

print(s.minimumEffortPath(heights))

