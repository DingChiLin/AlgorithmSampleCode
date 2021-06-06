class TopologicalSort: # by DFS (recursive)
    def __init__(self):
        self.ans = None
        self.index = None

    def dfs(self, node, edges, visited, curVisited):
        for v in edges[node]:
            if v in curVisited:
                return False
            if v not in visited:
                visited.add(v)
                curVisited.add(v)
                if not self.dfs(v, edges, visited, curVisited):
                    return False
                curVisited.remove(v)
        self.ans[self.index] = node      
        self.index -= 1
        return True

    def sort(self, nodes, edges):
        N = len(nodes)
        self.ans = [None for _ in range(N)]
        self.index = N - 1
        visited = set()
        curVisited = set()
        for n in nodes:
            if n not in visited:
                visited.add(n)
                curVisited.add(n)
                if not self.dfs(n, edges, visited, curVisited):
                    return []
                curVisited.remove(n)
        return self.ans

from collections import defaultdict, deque
class TopologicalSort2: # by Kahn's Algorithm
    def sort(self, nodes, edges):
        in_degree = defaultdict(int)
        out_edges = defaultdict(list)

        for u in edges:
            for v in edges[u]:
                in_degree[v] += 1
                out_edges[u].append(v)

        que = deque()
        for n in nodes:
            if in_degree[n] == 0:
                que.append(n)
        
        ans = []
        while que:
            u = que.popleft()
            ans.append(u)
            for v in out_edges[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    que.append(v)

        return ans if (len(ans) == len(nodes)) else []

topSort = TopologicalSort()
topSort2 = TopologicalSort2()

# graph1 with direction: left to right
# 2   1 - 4 - 7 
#  \ /   /
#   0   6    
#  / \ /
# 3 - 5

nodes = list(range(8))
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

print(topSort.sort(nodes, edges1)) # [3, 2, 0, 5, 6, 1, 4, 7]
print(topSort2.sort(nodes, edges1)) # [2, 3, 0, 1, 5, 6, 4, 7]

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
print(topSort.sort(nodes, edges2)) #[7, 6, 5, 3, 4, 2, 1, 0]
print(topSort2.sort(nodes, edges2)) #[0, 5, 6, 7, 2, 1, 3, 4]

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

print(topSort.sort(nodes, edges3)) # []
print(topSort2.sort(nodes, edges3)) # []
