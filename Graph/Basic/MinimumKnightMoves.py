from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        X, Y = abs(x), abs(y)
        que = deque([(0, 0, 0)])
        visited = set([(0, 0)])
        while que:
            x, y, d = que.popleft()
            if x == X and y == Y:
                return d
            for dx, dy in [[1,2], [1,-2], [2,1], [2,-1], [-1,2], [-1,-2], [-2,1], [-2,-1]]:
                nx, ny = abs(x + dx), abs(y + dy)
                if (nx, ny) not in visited and \
                    0 <= x <= 300 and \
                    0 <= y <= 300:
                    visited.add((nx, ny))
                    que.append((nx, ny, d + 1))