from collections import deque
from math import inf

class Solution:
    def bfs(self, N, adj_matrix, start, end):
        que = deque([(start, inf)])
        predecessor = [-1 for _ in range(N)]
        visited = set([start])
        while que:
            n, w = que.popleft()
            if n == end:
                return w, predecessor
            for nx in range(N):
                if adj_matrix[n][nx] != 0 and (nx not in visited):
                    visited.add(nx)
                    predecessor[nx] = n
                    que.append((nx, min(w, adj_matrix[n][nx])))
        return 0, []
 
    def get_residual(self, adj_matrix, weight, predecessor, start, end):
        n = end
        while n != start:
            nx = predecessor[n]
            adj_matrix[nx][n] -= weight
            adj_matrix[n][nx] += weight
            n = nx
 
    def max_flow(self, N, graph, start, end):
        adj_matrix = [[0 for _ in range(N)] for _ in range(N)]
        for x, y, w in graph:
            adj_matrix[x][y] = w

        ans = 0
        while True:
            weight, predecessor = self.bfs(N, adj_matrix, start, end)
            ans += weight
            if not weight:
                break
            self.get_residual(adj_matrix, weight, predecessor, start, end)

        print(adj_matrix)
        return ans

S = Solution()


'''
    > 1
  /2  | 1\ 
0    3|   > 4 
  \1  v 2/
    > 2 

ans: 3
'''

graph = [
    [0, 1, 2],
    [0, 2, 1], 
    [1, 2, 3], 
    [1, 4, 1], 
    [2, 4, 2]
]
N = 5
start = 0
end = 4
print(S.max_flow(N, graph, start, end))


'''
    > 1
  /4  | 5\ 
0    2|   > 4 
  \8  v 1/
    > 2 

ans: 5
'''

graph = [
    [0, 1, 4],
    [0, 2, 8], 
    [1, 2, 2], 
    [1, 4, 5], 
    [2, 4, 1]
]
N = 5
start = 0
end = 4
print(S.max_flow(N, graph, start, end))


'''
pic: http://alrightchiu.github.io/SecondRound/flow-networksmaximum-flow-ford-fulkerson-algorithm.html
ans: 17
'''

graph = [
    [0, 1, 9],
    [1, 2, 3], 
    [2, 5, 9], 
    [0, 3, 9], 
    [3, 4, 7],
    [4, 5, 8],
    [1, 3, 8],
    [3, 2, 7],
    [2, 4, 2],
    [4, 2, 4],
]
N = 6
start = 0
end = 5
print(S.max_flow(N, graph, start, end))
