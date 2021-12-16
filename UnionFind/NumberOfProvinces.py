from typing import List

class UnionFind:
    def __init__(self, N):
        self.father = [i for i in range(N)]
        self.rank = [1 for i in range(N)]       

    def root(self, n):
        if n != self.father[n]:
            self.father[n] = self.root(self.father[n])
        return self.father[n]

    def union(self, n1, n2):
        r1 = self.root(n1)
        r2 = self.root(n2)
        if r1 != r2:
            if self.rank[r1] < self.rank[r2]:
                self.father[r1] = r2
            elif self.rank[r1] > self.rank[r2]:
                self.father[r2] = r1
            else:
                self.father[r2] = r1
                self.rank[r1] += 1
            return True
        return False

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        UF = UnionFind(N)
        for i in range(N):
            for j in range(N):
                if isConnected[i][j]:
                    UF.union(i,j)
        
        return len(set([UF.root(x) for x in range(N)]))