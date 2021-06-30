from typing import List

# BFS
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        N = len(image)
        M = len(image[0])
        originalColor = image[sr][sc]

        if originalColor == newColor:
            return image

        que = deque()
        que.append((sr, sc))
        while(que):
            x, y = que.popleft()
            image[x][y] = newColor
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < M and image[nx][ny] == originalColor:
                    que.append((nx, ny))

        return image

# DFS
class Solution:
    def dfs(self, x, y, originalColor, newColor, image):
        N = len(image)
        M = len(image[0])
        image[x][y] = newColor
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and image[nx][ny] == originalColor:
                self.dfs(nx, ny, originalColor, newColor, image)
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        N = len(image)
        M = len(image[0])
        originalColor = image[sr][sc]

        if originalColor == newColor:
            return image

        self.dfs(sr, sc, originalColor, newColor, image)

        return image
