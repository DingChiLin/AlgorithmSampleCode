import collections
from typing import List
from collections import defaultdict

class Solution:
    def __init__(self):
        self.count = 0

    def dfs(self, n, parent, visited, edges, direction):
        if n != 0 and parent not in direction[n]:
            self.count += 1
        for child in edges[n]:
            if child not in visited:
                visited.add(child)
                self.dfs(child, n, visited, edges, direction)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = defaultdict(list)
        direction = defaultdict(set)

        for n1, n2 in connections:
            edges[n1].append(n2)
            edges[n2].append(n1)
            direction[n1].add(n2)

        self.count = 0
        self.dfs(0, -1, set([0]), edges, direction)
        return self.count

s = Solution()
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(s.minReorder(n, connections))