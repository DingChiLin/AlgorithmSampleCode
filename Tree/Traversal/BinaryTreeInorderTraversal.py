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

# Stack (general)
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stk = []
        curr = root
        while stk or curr:
            if curr:
                stk.append(curr)
                curr = curr.left
            else:
                node = stk.pop()
                ans.append(node.val)
                curr = node.right
        return ans

# Stack (simplest)
class Solution3:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stk = []
        curr = root
        ans = []
        while curr or stk:
            while curr:
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()
            ans.append(curr.val)
            curr = curr.right
        return ans
 
root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

S = Solution2()
print(S.inorderTraversal(root))