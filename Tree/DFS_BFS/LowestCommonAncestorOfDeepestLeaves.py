from typing import Optional
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def helper(self, node):
        if not node:
            return None, 0
        left_node, left_height = self.helper(node.left)
        right_node, right_height = self.helper(node.right)
        
        if left_height < right_height:
            return right_node, right_height + 1
        elif left_height > right_height:
            return left_node, left_height + 1
        else:
            return node, left_height + 1
    
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lca, h = self.helper(root)
        return lca