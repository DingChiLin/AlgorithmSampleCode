from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = []

    def dfs(self, node, remain, path):
        if remain == 0 and not node.left and not node.right:
            self.ans.append(path[:])
            return
        if not node:
            return
        if node.left:
            path.append(node.left.val)
            self.dfs(node.left, remain - node.left.val, path)
            path.pop()
        if node.right:
            path.append(node.right.val)
            self.dfs(node.right, remain - node.right.val, path)
            path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.dfs(root, targetSum - root.val, [root.val])
        return self.ans