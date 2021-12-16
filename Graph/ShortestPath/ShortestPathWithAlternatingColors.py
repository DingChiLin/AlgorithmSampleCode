from typing import List
from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph =  [[[] for j in range(n)] for i in range(2)]
        for n1, n2 in red_edges:
            graph[0][n1].append(n2)
        for n1, n2 in blue_edges:
            graph[1][n1].append(n2)

        self.visited = [[False for j in range(n)] for i in range(2)]
        queue = deque()
        queue.append((0, 0)) #(color [0=red, 1=blue], node)
        queue.append((1, 0))
        record = [float('inf') for i in range(n)]
        step = 0
        while queue:
            for _ in range(len(queue)):
                color, n = queue.popleft()
                if not self.visited[color][n]:
                    record[n] = min(record[n], step)
                    self.visited[color][n] = True
                    for next_node in graph[1-color][n]:
                        if not self.visited[1-color][next_node]:
                            queue.append((1-color, next_node))
            step += 1
        return [n if n < float('inf') else -1 for n in record]