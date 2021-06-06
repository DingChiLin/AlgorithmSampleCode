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
            return True
        return False

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        queries = sorted([query[2], query[0], query[1], i] for i, query in enumerate(queries))
        edges = sorted([[w, u, v] for u, v, w in edgeList])

        UF = UnionFind(n) 
        ans = [None] * len(queries)
        edgeIndex = 0
        for w, u, v, i in queries:
            while edgeIndex < len(edges) and edges[edgeIndex][0] < w:
                UF.union(edges[edgeIndex][1], edges[edgeIndex][2])
                edgeIndex += 1
            ans[i] = (UF.root(u) == UF.root(v))
                
        return ans

s = Solution()
n = 3
edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]]
queries = [[0,1,2],[0,2,5]]
print(s.distanceLimitedPathsExist(n, edgeList, queries))