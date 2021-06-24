from typing import List

class Solution:
    def __init__(self):
        self.ans = []
    
    def helper(self, graph, node, target, path):
        if (node == target):
            self.ans.append(path)
            return
        for n in graph[node]:
            path.append(n)
            self.helper(graph, n, target, path[:])
            path.pop()
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans = []
        self.helper(graph, 0, len(graph)-1, [0])
        return self.ans