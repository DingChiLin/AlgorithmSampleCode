from typing import List
from collections import defaultdict

class TopologicalSort: # by DFS (recursive)
    def __init__(self):
        self.ans = None
        self.index = None

    def dfs(self, node, edges, visited, curVisited):
        for v in edges[node]:
            if v in curVisited:
                return False
            if v not in visited:
                visited.add(v)
                curVisited.add(v)
                if not self.dfs(v, edges, visited, curVisited):
                    return False
                curVisited.remove(v)
        self.ans[self.index] = node      
        self.index -= 1
        return True

    def sort(self, N, edges):
        self.ans = [None for _ in range(N)]
        self.index = N - 1
        visited = set()
        curVisited = set()
        for n in range(N):
            if n not in visited:
                visited.add(n)
                curVisited.add(n)
                if not self.dfs(n, edges, visited, curVisited):
                    return []
                curVisited.remove(n)
        return self.ans

class Solution:
    def countColor(self, colors, edges, sortedNodes, chosenColor):
        colorCount = [0 for i in range(len(colors))]
        for n in sortedNodes:
            tmp = 0
            for nx in edges[n]:
                tmp = max(tmp, colorCount[nx])
            colorCount[n] = tmp + (colors[n] == chosenColor)

        return max(colorCount)

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adjListEdges = defaultdict(list)
        for u, v in edges:
            adjListEdges[u].append(v)
        N = len(colors)
        sortedNodes = TopologicalSort().sort(N, adjListEdges)
        if sortedNodes == []: # cycle
            return -1

        sortedNodes.reverse() # reverse order
        colors = [ord(c) - 97 for c in colors] # string to int array
        ans = 0
        for i in set(colors):
            ans = max(ans, self.countColor(colors, adjListEdges, sortedNodes, i))

        return ans

s = Solution()
colors = "abaca"
edges = [[0,1],[0,2],[2,3],[3,4]]

colors = "a"
edges = [[0,0]]
print(s.largestPathValue(colors, edges))