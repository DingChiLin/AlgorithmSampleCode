from typing import List
from collections import defaultdict

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

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i, g in enumerate(group):
            if g == -1:
                group[i] = m
                m += 1

        group_edges = defaultdict(set)
        group_nodes = defaultdict(list)
        node_edges = defaultdict(list)
        for n, items in enumerate(beforeItems):
            group_nodes[group[n]].append(n)
            for item in items:
                if group[item] != group[n]:
                    group_edges[group[item]].add(group[n])
                else:
                    node_edges[item].append(n)
        group_order = TopologicalSort().sort(list(range(m)), group_edges)
        if group_order == []:
            return []

        ans = []
        for g in group_order:
            nodes = group_nodes[g]
            if not nodes:
                continue
            ordered_nodes = TopologicalSort().sort(nodes, node_edges)
            if ordered_nodes == []:
                return []
            for n in ordered_nodes:
                ans.append(n)

        return ans

s = Solution()
n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]


n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3],[],[4],[]]

n = 5
m = 5
group = [2,0,-1,3,0]
beforeItems = [[2,1,3],[2,4],[],[],[]]
print(s.sortItems(n, m, group, beforeItems))