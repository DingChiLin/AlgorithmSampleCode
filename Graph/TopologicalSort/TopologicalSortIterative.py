class TopologicalSort: # by DFS (iterative)
    def dfs_stack(self, N, node, adj_list, orders, state):
        if state[node] == 2:
            return False

        stk = [[node, 0]] # (parent, node, child_index)
        while stk:
            n, c_id = stk[-1] # current node
            if state[n] == 2: # already visited
                stk.pop()
                continue
            
            has_unvisited_child = False
            for i in range(c_id, len(adj_list[n])):
                nxt = adj_list[n][i]
                stk[-1][1] += 1 # c_id + 1
                if state[nxt] == 2:
                    continue
                if state[nxt] == 1: # find cycle
                    return True
                has_unvisited_child = True
                state[nxt] = 1
                stk.append([nxt, 0])
                break
            if not has_unvisited_child:
                stk.pop() # pop out this node
                state[n] = 2
                orders.append(n)
        return False

    def sort(self, N, edges):
        orders = []
        state = [0 for i in range(N)] # 0: unvisited 1: cur_visited 2: visited
        for n in range(N):
            if self.dfs_stack(N, n, edges, orders, state):
                return []
        return orders[::-1]

topSort = TopologicalSort()

# graph1 with direction: left to right
# 2   1 - 4 - 7 
#  \ /   /
#   0   6    
#  / \ /
# 3 - 5

N = 8
edges1 = {
    0: [1, 5],
    1: [4],
    2: [0],
    3: [0, 5],
    4: [7],
    5: [6],
    6: [4],
    7: []
}

print(topSort.sort(N, edges1)) # [3, 2, 0, 5, 6, 1, 4, 7]

# graph2 with direction: left to right
# 0
#    1 
#  / 
# 6 - 3 - 4 
#  \ ___ / 
# 5 - 2
# 7

edges2 = {
    0:[],
    1:[],
    2:[],
    3:[4],
    4:[],
    5:[2],
    6:[1, 3, 4],
    7:[]
}
print(topSort.sort(N, edges2)) #[7, 6, 5, 3, 4, 2, 1, 0]

# graph3 with direction: left to right (impossible)
# 0
#    1 
#  / 
# 6 - 3 - 4
#  \ ___ /    # direction:  <--
# 5 - 2
# 7

edges3 = {
    0:[],
    1:[],
    2:[],
    3:[4],
    4:[6],
    5:[2],
    6:[1, 3],
    7:[]
}

print(topSort.sort(N, edges3)) # []
