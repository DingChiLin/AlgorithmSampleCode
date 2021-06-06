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
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        for v, u in prerequisites:
            edges[u].append(v)
        
        return TopologicalSort().sort(numCourses, edges)

s = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(s.canFinish(numCourses, prerequisites))