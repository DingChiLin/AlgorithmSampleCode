from typing import List
from collections import defaultdict

class Solution:
    def dfs(self, node, edges, vistied, curVisited):
        for n in edges[node]:
            if n in curVisited:
                return True # find cycle
            elif n not in vistied:
                vistied.add(n)
                curVisited.add(n)
                if self.dfs(n, edges, vistied, curVisited):
                    return True
                curVisited.remove(n)

        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        for u, v in prerequisites:
            edges[u].append(v)

        visited = set()
        for i in range(numCourses):
            if i not in visited:
                visited.add(i)
                if self.dfs(i, edges, visited, set([i])): # find cycle
                    return False

        return True

s = Solution()
numCourses = 3
prerequisites = [[0,1],[0,2],[1,2]]
print(s.canFinish(numCourses, prerequisites))