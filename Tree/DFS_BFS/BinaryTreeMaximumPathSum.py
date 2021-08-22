from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        def search(node):
            if node == None:
                return 0
            left_max = max(search(node.left), 0) # 0 可以想成不使用他
            right_max = max(search(node.right), 0)
            self.max_sum = max(self.max_sum, left_max + right_max + node.val)

            return max(left_max, right_max) + node.val
        search(root)

        return self.max_sum
