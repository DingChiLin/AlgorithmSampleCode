from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root in [p, q]:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if left:
            return left
        else:
            return right

# Iterative
from collections import defaultdict
class Solution:
    def find_parent(self, root):
        parents = defaultdict(TreeNode)
        parents[root] = None
        stk = [root]        
        while stk:
            node = stk.pop()
            if node.left:
                parents[node.left] = node
                stk.append(node.left)
            if node.right:
                parents[node.right] = node
                stk.append(node.right)
        return parents 

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = self.find_parent(root)
        ancestors = set()
        while q != None:
            ancestors.add(q)
            q = parents[q]
        while p != None:
            if p in ancestors:
                return p
            p = parents[p]

'''
Tree:
     4
   2   6
  1 3 5 7  
'''

Node1 = TreeNode(1)
Node2 = TreeNode(2)
Node3 = TreeNode(3)
Node4 = TreeNode(4)
Node5 = TreeNode(5)
Node6 = TreeNode(6)
Node7 = TreeNode(7)

root = Node4
root.left = Node2
root.right = Node6
Node2.left = Node1
Node2.right = Node3
Node6.left = Node5
Node6.right = Node7

S = Solution()
print(S.lowestCommonAncestor(root, Node7, Node6).val)
