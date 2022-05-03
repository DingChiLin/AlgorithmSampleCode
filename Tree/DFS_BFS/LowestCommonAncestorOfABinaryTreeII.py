class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# return counter
class Solution:
    def helper(self, node, p, q):
        if not node:
            return None, 0
        left, lcnt = self.helper(node.left, p, q)
        right, rcnt = self.helper(node.right, p, q)
        if left and right:
            return node, 2
        if left:
            if lcnt == 2:
                return left, 2
            if node in [p, q]:
                return node, 2
            return left, lcnt

        if right:
            if rcnt == 2:
                return right, 2
            if node in [p, q]:
                return node, 2
            return right, rcnt

        if node in [p, q]:
            return node, 1

        return None, 0

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca, cnt = self.helper(root, p, q)
        return lca if cnt == 2 else None


# use global counter
class Solution:
    def helper(self, root, p, q):
        if not root:
            return None
        
        left = self.helper(root.left, p, q)
        right = self.helper(root.right, p, q)
        if left and right:
            return root

        if root in [p, q]:
            self.counter += 1
            return root
        else:
            if left:
                return left
            if right:
                return right         
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.counter = 0
        lca = self.helper(root, p, q)
        return lca if self.counter == 2 else None
