from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorderIndexMap = {n: i for i, n in enumerate(inorder)}
        def helper(start, end):
            if start > end:
                return None
            n = postorder.pop()
            node = TreeNode(n)
            index = inorderIndexMap[n]
            node.right = helper(index+1, end)
            node.left = helper(start, index-1)
            return node

        return helper(0, len(inorder)-1)