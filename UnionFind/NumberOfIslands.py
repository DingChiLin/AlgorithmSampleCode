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
    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])
        u = UnionFind(N * M)
        for i in range(N):
            for j in range(M):
                if (grid[i][j] == "1"):
                    node = i * M + j
                    if (i < N-1):
                        if (grid[i + 1][j] == "1"):
                            next1 = (i + 1) * M + j
                            u.union(node, next1)
                    if (j < M-1):
                        if (grid[i][j + 1] == "1"):
                            next2 = i * M + (j + 1)
                            u.union(node, next2)

        ans = set()
        for i in range(N):
            for j in range(M):
                if (grid[i][j] == "1"):
                    ans.add(u.root(i * M + j))

        return len(ans)

s = Solution()
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(s.numIslands(grid))