class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# Simple DFS
class Solution:
    def __init__(self):
        self.maxDepth = 0

    def dfs(self, node, depth):
        self.maxDepth = max(self.maxDepth, depth)
        for child in node.children:
            self.dfs(child, depth + 1)

    def maxDepth(self, root: 'Node') -> int:
        self.dfs(root, 1)
        return self.maxDepth

# Backtracking
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 0
        for child in root.children:
            depth = max(depth, self.maxDepth(child))
        return depth + 1
