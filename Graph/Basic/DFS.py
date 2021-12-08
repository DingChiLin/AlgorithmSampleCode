edges = {
	0: [1],
	1: [2, 3],
	2: [4],
	3: [4],
  4: []
}

# DFS
def dfs(node, edges, visited):
    print(node)
    for nx in edges[node]:
        if nx not in visited:
            visited.add(nx)
            dfs(nx, edges, visited)

dfs(0, edges, set())
