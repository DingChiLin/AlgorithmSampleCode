class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS
class Solution:
    def __init__(self):
        self.ans = 0

    def dfs(self, node, depth):
        self.ans = max(self.ans, depth)
        if node.left:
            self.dfs(self.left, depth + 1)
        if node.right:
            self.dfs(self.right, depth + 1)

    def maxDepth(self, root: TreeNode) -> int:
        self.dfs(root, 1)
        return self.ans

# BFS
from collections import deque
class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = deque([(root, 1)])
        ans = 0
        while que:
            node, depth = que.popleft()
            ans = max(ans, depth)
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))
        return ans
