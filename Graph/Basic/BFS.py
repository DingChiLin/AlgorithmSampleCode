from collections import deque
edges = {
	0: [1],
	1: [2, 3],
	2: [4],
	3: [4],
  4: []
}

# BFS
def bfs(edges):
	que = deque()
	que.append((0, 0))  # (node, depth))
	visited = set()

	while que:
		n, d = que.popleft()
		print("node/depth", n, d)
		for nx in edges[n]:
			if nx not in visited:
				visited.add(nx)
				que.append((nx, d+1))

bfs(edges)
