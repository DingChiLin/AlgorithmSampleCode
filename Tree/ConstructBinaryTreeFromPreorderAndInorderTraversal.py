from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorderIndexMap = {v: i for i, v in enumerate(inorder)}
        preorderQueue = deque(preorder)
        def helper(start, end):
            if start > end:
                return None

            n = preorderQueue.popleft()
            node = TreeNode(n)
            index = inorderIndexMap[n]
            node.left = helper(start, index-1)
            node.right = helper(index+1, end)
            return node

        return helper(0, len(inorder)-1)