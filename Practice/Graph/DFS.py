from collections import defaultdict

class DFS:
    def traversal(self, edges, start):
        visited = set([start])
        def dfs(u):
            print(u)
            for v in edges[u]:
                if v not in visited:
                    visited.add(v)
                    dfs(v) 
        dfs(0)
        return None


# Graph: Undirected
#     1 -- 3 -- 5
#    /   /  \  /
#  0 -- 2 -- 4

# Adjacency List
edges = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3, 4],
    3: [1, 2, 4, 5],
    4: [2, 3, 5],
    5: [3, 4]
}

print(DFS().traversal(edges, 0))


