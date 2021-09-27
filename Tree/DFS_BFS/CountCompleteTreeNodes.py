class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leftHeight(self, node):
        if not node:
            return -1
        else:
            return 1 + self.leftHeight(node.left)

    def rightHeight(self, node):
        if not node:
            return -1
        else:
            return 1 + self.rightHeight(node.right)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        lh = self.leftHeight(root)
        if lh == 0:
            return 1

        # count the depth of the rightmost child of the left part of root
        rh = self.rightHeight(root.left)

        if rh == lh - 1: # left is full
            return 1 + (2 ** lh - 1) + self.countNodes(root.right)
        else: # left is not full
            return 1 + self.countNodes(root.left) + (2 ** (lh - 1) - 1)