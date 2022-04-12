from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursion
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def dfs(node):
            if not node:
                return
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ans

# Stack (general)
class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stk = []
        curr = root
        while stk or curr:
            if curr:
                stk.append(curr)
                ans.append(curr.val)
                curr = curr.left
            else:
                node = stk.pop()
                curr = node.right
        return ans

# Stack (simplest)
class Solution3:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stk = [root]
        ans = []
        while stk:
            n = stk.pop()
            ans.append(n.val)
            if n.right:
                stk.append(n.right)
            if n.left:
                stk.append(n.left)
        return ans

# Stack Space O(1) (Morris traversal)
class Solution4:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node, output = root, []
        while node:  
            if not node.left: 
                output.append(node.val)
                node = node.right 
            else: 
                predecessor = node.left 

                while predecessor.right and predecessor.right is not node: 
                    predecessor = predecessor.right 

                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node  
                    node = node.left  
                else:
                    predecessor.right = None
                    node = node.right         

        return output

root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

S = Solution2()
print(S.preorderTraversal(root))