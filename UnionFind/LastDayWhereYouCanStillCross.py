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
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        N = len(cells)
        u = UnionFind((row * col + 2))
        start = 0
        end = row * col + 1

        for i in range(col):
            u.union(start, i+1)

        for i in range(col):
            u.union(end, (row - 1) * col + 1 + i)

        Graph = [[1 for _ in range(col)] for _ in range(row)]

        for i in range(N-1, -1, -1):
            x, y = cells[i]
            x, y = x-1, y-1
            encode = x * col + y + 1
            
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < row and 0 <= ny < col:
                    if Graph[nx][ny] == 0:
                        u.union(encode, nx * col + ny + 1)
                Graph[x][y] = 0

                if u.root(start) == u.root(end):
                    return i

s = Solution()
row = 3
col = 3
cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]

print(s.latestDayToCross(row, col, cells))