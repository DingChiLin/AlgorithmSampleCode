from collections import defaultdict
  
class Bridge:
    def dfs(self, parent, node, edges, node_id, lowest_node, ap): #, edges_stk, bcc_edges):
        children = 0
        node_id[node] = lowest_node[node] = self.time
        self.time += 1
        for nxt in edges[node]:
            if nxt == parent:
                continue
            if node_id[nxt] == -1: # not seen before
                children += 1
                # edges_stk.append((node, nxt)) #
                self.dfs(node, nxt, edges, node_id, lowest_node, ap) #, edges_stk, bcc_edges)
                lowest_node[node] = min(lowest_node[node], lowest_node[nxt])

                if ((parent != -1 and lowest_node[nxt] >= node_id[node]) or
                     (parent == -1 and children >= 2)):
                    ap.append(node)
                    
                    # while (edges_stk[-1][0] != node or edges_stk[-1][1] != nxt): #
                    #     bcc_edges[self.bcc_cnt].append(edges_stk.pop()) #
                    
                    # bcc_edges[self.bcc_cnt].append(edges_stk.pop()) #
                    # self.bcc_cnt += 1 #
            else:
                if (node_id[nxt] < node_id[node]):
                    lowest_node[node] = min(lowest_node[node], node_id[nxt])
                    # edges_stk.append((node, nxt)) #

    def find_articulation_point(self, N, graph):
        self.time = 0
        self.bcc_cnt = 0
        edges = defaultdict(list)
        for u, v in graph:
            edges[u].append(v)
            edges[v].append(u)

        node_id = [-1 for i in range(N)]
        lowest_node = [-1 for i in range(N)]
        ap = []
        # bcc_edges = defaultdict(list)
        # edges_stk = []
        for n in range(N):
            if node_id[n] == -1:
                self.dfs(-1, n, edges, node_id, lowest_node, ap) #, edges_stk, bcc_edges)
                # while edges_stk: #
                #     bcc_edges[self.bcc_cnt].append(edges_stk[-1]) #
                #     edges_stk.pop() #
                # self.bcc_cnt += 1 #
        print(ap)
        # print(self.bcc_cnt)
        # print(bcc_edges) 
 
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
print(BG.find_articulation_point(N, graph))