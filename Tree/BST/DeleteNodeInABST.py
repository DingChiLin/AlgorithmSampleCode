class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getPredecessor(self, node):
        pred = node.left
        while pred.right:
            pred = pred.right
        return pred

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                pred = self.getPredecessor(root)
                root.val = pred.val
                root.left = self.deleteNode(root.left, pred.val)
        return root
