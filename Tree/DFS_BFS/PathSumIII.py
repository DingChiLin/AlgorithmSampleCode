from typing import Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = 0

    def dfs(self, node, preSum, counter, target):
        preSum += node.val
        self.ans += counter[preSum - target]

        counter[preSum] += 1
        if node.left:
            self.dfs(node.left, preSum, counter, target) 
        if node.right:
            self.dfs(node.right, preSum, counter, target) 
        counter[preSum] -= 1

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        counter = defaultdict(int)
        counter[0] = 1
        self.dfs(root, 0, counter, targetSum)
        return self.ans