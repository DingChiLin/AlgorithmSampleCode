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

# Stack (general: trick of inverse inorder traversal)
class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stk = []
        curr = root
        while stk or curr:
            if curr:
                stk.append(curr)
                ans.append(curr.val)
                curr = curr.right
            else:
                node = stk.pop()
                curr = node.left
        return ans[::-1]

# Stack (formal)
class Solution3:
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

root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

S = Solution2()
print(S.postorderTraversal(root))