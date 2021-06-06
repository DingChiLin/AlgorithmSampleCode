from typing import List

class Solution:
    def dfs(self, node, edges, visited):
        if (len(visited) == len(edges)):
            return True

        for child in edges[node]:
            if child not in visited:
                visited.add(child)
                if self.dfs(child, edges, visited):
                    return True

        return False

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        return self.dfs(0, rooms, visited)

s = Solution()
rooms = [[1,3],[3,0,1],[2],[0]]
print(s.canVisitAllRooms(rooms))