from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = True

    def helper(self, node):
        if not node:
            return 0
        leftHeight = self.helper(node.left)
        rightHeight = self.helper(node.right)
        if abs(leftHeight - rightHeight) > 1:
            self.ans = False
        return max(leftHeight, rightHeight) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.helper(root)
        return self.ans