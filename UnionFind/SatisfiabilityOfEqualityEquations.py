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
    def equationsPossible(self, equations: List[str]) -> bool:
        equals = []
        unequals = []
        for eq in equations:
            if eq[1] == '=':
                equals.append((ord(eq[0]) - 97, ord(eq[3]) - 97))
            else:
                unequals.append((ord(eq[0]) - 97, ord(eq[3]) - 97))

        u = UnionFind(26)
        for (a, b) in equals:
            u.union(a, b)
        
        for (a, b) in unequals:
            if u.root(a) == u.root(b):
                return False

        return True

s = Solution()
equations = ["a==b","b!=c","c==a"]
print(s.equationsPossible(equations))