from typing import List

class UnionFind:
    def __init__(self, N):
        self.fathers = [i for i in range(N)]
        self.ranks = [1] * N
        self.value = [-1] * N
        
    def root(self, n):
        v = 1
        while n != self.fathers[n]:
            v *= self.value[n]
            n = self.fathers[n]
        return (n, v)
    
    def union(self, x, y, v):
        rx, vx = self.root(x)
        ry, vy = self.root(y)
        rv = (v / vx) * vy
        if rx == ry:
            return False
        
        if self.ranks[rx] > self.ranks[ry]:
            self.fathers[ry] = rx
            self.value[ry] = 1/rv    
            self.ranks[rx] = max(self.ranks[rx], self.ranks[ry] + 1)
        else:
            self.fathers[rx] = ry
            self.value[rx] = rv    
            self.ranks[ry] = max(self.ranks[rx] + 1, self.ranks[ry])      
        return True
        
class Solution:
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = set()
        for x, y in equations:
            nodes.add(x)
            nodes.add(y)
            
        mapping = {a: i for i, a in enumerate(nodes)}
        N = len(nodes)
        U = UnionFind(N)
        
        for i in range(len(equations)):
            x, y = equations[i]
            v = values[i]
            U.union(mapping[x], mapping[y], v)
        
        ans = []
        for qx, qy in queries:
            if qx not in nodes or qy not in nodes:
                ans.append(-1)
                continue
            rx, vx = U.root(mapping[qx])
            ry, vy = U.root(mapping[qy])
            if rx != ry:
                ans.append(-1)
            else:
                ans.append(vx/vy)
        return ans

s = Solution()
equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
print(s.calcEquation(equations, values, queries))