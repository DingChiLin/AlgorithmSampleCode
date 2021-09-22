from typing import List
from collections import deque

class Solution:   
    def findNexts(self, x, y, maze):
        nxts = []
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = x, y
            while 0 <= nx+dx < len(maze) and \
                0 <= ny+dy < len(maze[0]) and \
                maze[nx+dx][ny+dy] != 1:
                nx += dx
                ny += dy
            nxts.append((nx, ny))
        return nxts
        
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        que = deque([tuple(start)]) 
        while que:
            x, y = que.popleft()
            if [x, y] == destination:
                return True
            nxts = self.findNexts(x, y, maze)
            for nxt in nxts:
                if nxt not in visited:
                    visited.add(nxt)
                    que.append(nxt)
            
        return False