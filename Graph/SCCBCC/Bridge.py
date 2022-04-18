from collections import defaultdict
  
class Bridge:
    def dfs(self, parent, node, edges, node_stk, node_id, lowest_node, bridges, bcc_group):
        node_id[node] = lowest_node[node] = self.time
        self.time += 1
        node_stk.append(node)
        for nxt in edges[node]:
            if nxt == parent:
                continue
            if node_id[nxt] == -1: # not seen before
                self.dfs(node, nxt, edges, node_stk, node_id, lowest_node, bridges, bcc_group)
            lowest_node[node] = min(lowest_node[node], lowest_node[nxt])
 
        if (lowest_node[node] == node_id[node]):
            if parent != -1:
                bridges.append((parent, node))

            while node_stk and node_stk[-1] != node:
                bcc_group[node_stk[-1]] = node
                node_stk.pop()
            bcc_group[node_stk[-1]] = node
            node_stk.pop()

    def find_bridge(self, N, graph):
        self.time = 0
        edges = defaultdict(list)
        for u, v in graph:
            edges[u].append(v)
            edges[v].append(u)

        node_id = [-1 for i in range(N)]
        lowest_node = [-1 for i in range(N)]
        bridges = []
        bcc_group = [-1 for i in range(N)]
        for n in range(N):
            if node_id[n] == -1:
                self.dfs(-1, n, edges, [], node_id, lowest_node, bridges, bcc_group)
        return bridges, bcc_group


'''
0

           4        10
         /   \     /  \
1 - 2 - 3     5 - 7 -  8 
         \   /     \  /
           6        9 - 14
           |
           11 - 12 - 13

15 - 16 - 17 - 18
      \________/
'''
N = 19
graph = [
    [1, 2],
    [2, 3],
    [3, 4], [4, 5], [5, 6], [6, 3],
    [6, 11],
    [11, 12],
    [12, 13],
    [5, 7],
    [7, 8], [8, 9], [9, 7], [7, 10], [10, 8],
    [9, 14],
    [15, 16],
    [16, 17],
    [18, 17],
    [16, 18]
]

BG = Bridge()
print(BG.find_bridge(N, graph))