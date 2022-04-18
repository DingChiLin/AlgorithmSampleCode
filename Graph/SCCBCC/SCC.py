from collections import defaultdict

class StronglyConnectedComponent: # by DFS (recursive)
    def dfs1(self, node, edges, node_order, visited):
        visited.add(node)
        for nxt in edges[node]:
            if nxt not in visited: 
                self.dfs1(nxt, edges, node_order, visited)
        node_order.append(node)

    def dfs2(self, node, rev_edges, visited, scc_index, scc_group, scc_edges):
        scc_group[node] = scc_index
        visited.add(node)
        for nxt in rev_edges[node]:
            if nxt not in visited:
                self.dfs2(nxt, rev_edges, visited, scc_index, scc_group, scc_edges)
            else:
                if scc_group[nxt] != scc_index:
                    scc_edges[scc_group[nxt]].append(scc_index)

    def find(self, N, graph):
        edges = defaultdict(list)
        rev_edges = defaultdict(list)
        for u, v in graph:
            edges[u].append(v)
            rev_edges[v].append(u)
        
        # dfs1
        visited = set()
        node_order = []
        for n in range(N):
            if n not in visited:
                self.dfs1(n, edges, node_order, visited)

        # dfs2
        scc_group = [None for i in range(N)]
        scc_cnt = 0
        scc_edges = defaultdict(list)
        visited = set()
        for i in range(N-1, -1, -1):
            n = node_order[i]
            if n not in visited:
                self.dfs2(n, rev_edges, visited, scc_cnt, scc_group, scc_edges)
                scc_cnt += 1

        return scc_cnt, scc_group, scc_edges
'''
0

            > 4 \        10
           /     >      >  >
1 -> 2 -> 3       5 -> 7 -> 8 
           <     /      <  <
            \ 6 <         9 -> 14
              |
              v
              11 -> 12 <-> 13

15 -> 16 <-> 17 <- 18
'''
N = 19
graph = [
    [1, 2],
    [2, 3],
    [3, 4], [4, 5], [5, 6], [6, 3],
    [6, 11],
    [11, 12],
    [12, 13], [13, 12],
    [5, 7],
    [7, 8], [8, 9], [9, 7], [7, 10], [10, 8],
    [9, 14],
    [15, 16],
    [16, 17], [17, 16],
    [18, 17]
]

SCC = StronglyConnectedComponent()
print(SCC.find(N, graph)) # []
