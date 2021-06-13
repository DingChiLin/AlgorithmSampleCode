from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursion
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            ans.append(node.val)
        dfs(root)
        return ans

# Stack
class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return

        ans = []
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            right = stack[-1].right
            if (right):
                curr = right
            else:
                node = stack.pop()
                while (stack and stack[-1].right == node):
                    ans.append(node.val)
                    node = stack.pop()
                ans.append(node.val)
        return ans