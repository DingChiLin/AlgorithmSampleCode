from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from math import inf

class Solution:
    def check(self, node, lower, upper):
        if not node:
            return True
        if lower < node.val < upper:
            return self.check(node.left, lower, node.val) and \
                   self.check(node.right, node.val, upper) 
        else:
            return False

    def isValidBST(self, root: TreeNode) -> bool:
        return self.check(root, -inf, inf)