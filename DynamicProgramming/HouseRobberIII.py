class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        def rob_plan(node):
            if not node:
                return 0, 0
            rob_left, rest_left = rob_plan(node.left)
            rob_right, rest_right = rob_plan(node.right)
            rob = node.val + rest_left + rest_right
            stop = max(rob_left, rest_left) + max(rob_right, rest_right)
            return rob, stop
            
        rob, rest =  rob_plan(root)
        return max(rob, rest)
