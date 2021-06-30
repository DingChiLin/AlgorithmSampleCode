from typing import List

# DFS
class Solution:
    def dfs(self, node, edges, visited):
        for child in edges[node]:
            if child not in visited:
                visited.add(child)
                self.dfs(child, edges, visited)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        self.dfs(0, rooms, visited)
        return len(visited) == len(rooms)

# BFS
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        que = deque([0])
        visited = set([0])
        
        while que:
            node = que.popleft()
            for child in rooms[node]:
                if child not in visited:
                    visited.add(child)
                    que.append(child)
          
        return len(visited) == len(rooms)

s = Solution()
rooms = [[1,3],[3,0,1],[2],[0]]
print(s.canVisitAllRooms(rooms))