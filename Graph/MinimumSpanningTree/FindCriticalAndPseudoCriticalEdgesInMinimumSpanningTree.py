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

# Kruskal
class MST:
    def find(self, N, edges, need = None, escape = None):
        UF = UnionFind(N) # create enough space for union find array
        weight = 0
        if need:
            w, u, v, id = edges[need]
            UF.union(u, v)
            weight += w

        for i, edge in enumerate(edges):
            if (i == escape):
                continue
            w, u, v, id = edge
            if UF.union(u, v):
                weight += w
        return weight

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = sorted([[edge[2], edge[0], edge[1], i] for i, edge in enumerate(edges)])
        MTree = MST()
        weight = MTree.find(n, edges)
        critical = []
        pseudoCritical = []
        for i in range(len(edges)):
            w1 = MTree.find(n, edges, i, i) # use i
            w2 = MTree.find(n, edges, None, i) # not use i
            id = edges[i][3]
            if (w2 != weight):
                critical.append(id)
            elif (w1 == weight and w2 == weight):
                pseudoCritical.append(id)

        return [critical, pseudoCritical]

s = Solution()
n = 6
edges = [[0,1,1],[1,2,1],[0,2,1],[2,3,4],[3,4,2],[3,5,2],[4,5,2]]
print(s.findCriticalAndPseudoCriticalEdges(n, edges)) # [[3], [0, 2, 1, 4, 5, 6]]