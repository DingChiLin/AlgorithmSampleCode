from typing import List

class UnionFind:
    def __init__(self, N, M):
        self.nodes = [i for i in range(N*M)]
        self.size = [1 for _ in range(N*M)]
        self.tops = [False for _ in range(N*M)]
        for i in range(M):
            self.tops[i] = True

    def root(self, n):
        if n != self.nodes[n]:
            self.nodes[n] = self.root(self.nodes[n])
        return self.nodes[n]

    def union(self, n1, n2):
        r1 = self.root(n1)
        r2 = self.root(n2)
        if r1 != r2:
            if self.size[r1] < self.size[r2]:
                self.nodes[r1] = r2
                self.size[r2] += self.size[r1]
                self.tops[r2] = (self.tops[r1] or self.tops[r2])
            else:
                self.nodes[r2] = r1
                self.size[r1] += self.size[r2]
                self.tops[r1] = (self.tops[r1] or self.tops[r2])
            return True
        else:
            return False

class Solution:
    def __init__(self):
        self.moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def valid(self, x, y, N, M):
        return (0 <= x < N and 0 <= y < M)

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        N = len(grid)
        M = len(grid[0])
        u = UnionFind(N, M)

        for (x, y) in hits:
            if grid[x][y] == 1:
                grid[x][y] *= -1

        for x in range(N):
            for y in range(M):
                node = x * M + y
                if grid[x][y] == 1:
                    nexts = []
                    if x < N-1 and grid[x+1][y] == 1:
                        nexts.append((x + 1) * M + y)
                    if y < M-1 and grid[x][y+1] == 1:
                        nexts.append(x * M + (y + 1))
                    for next in nexts:
                        u.union(node, next)

        ans = []
        for (x, y) in reversed(hits):
            if (grid[x][y] == 0):
                ans.append(0)
                continue
            grid[x][y] = 1

            non_top_size = 0
            node = x * M + y
            r = u.root(node)
            has_top = u.tops[r]

            for (dx, dy) in self.moves:
                nx = x + dx
                ny = y + dy
                if self.valid(nx, ny, N, M) and grid[nx][ny] == 1:
                    next_node = nx * M + ny

                    nr = u.root(next_node)
                    next_is_top = u.tops[nr]
                    if next_is_top:
                        has_top = True
                    
                    sz = u.size[nr]
                    if u.union(node, next_node) and not next_is_top:
                        non_top_size += sz

            if has_top:
                ans.append(non_top_size)
            else:
                ans.append(0)

        ans.reverse()
        return ans

s = Solution()
grid = [[1,1,0,1,0],[1,1,0,1,1],[0,0,0,1,1],[0,0,0,1,0],[0,0,0,0,0],[0,0,0,0,0]]
hits = [[5,1],[1,3]]

grid = [[1],[1],[1],[1],[1]]
hits = [[3,0],[4,0],[1,0],[2,0],[0,0]]
print(s.hitBricks(grid, hits))
