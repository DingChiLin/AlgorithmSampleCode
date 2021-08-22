from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursion
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        dfs(root)
        return ans

# Stack
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return

        ans = []
        current = root
        stack = []
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                ans.append(current.val)
                current = current.right
            else:
                break
        return ans