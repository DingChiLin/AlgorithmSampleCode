class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        self.k = k
        self.num = 0
        def helper(node):
            if node.left != None:
                helper(node.left)

            self.k = self.k-1
            if(self.k == 0):
                self.num = node.val

            if node.right != None:
                helper(node.right)
                
        helper(root)
        return self.num