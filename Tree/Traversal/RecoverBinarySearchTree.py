class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.first = None
        self.second = None
        self.prev = None
         
        def helper(node):
            if not node:
                return
            helper(node.left)
            if (not self.first) and self.prev and self.prev.val > node.val:
                self.first = self.prev
            if self.first and self.prev and self.prev.val > node.val:
                self.second = node
            self.prev = node
            helper(node.right)

        helper(root)
        tmp = self.first.val
        self.first.val = self.second.val
        self.second.val = tmp
        return