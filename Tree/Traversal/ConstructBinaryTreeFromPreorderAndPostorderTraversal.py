from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        index = {}
        for i in range(len(post)):
            index[post[i]] = i

        def helper(i, j, n):
            if (n <= 0):
                return
            if (n == 1):
                return TreeNode(pre[i])
            node = TreeNode(pre[i])
            k = index[pre[i+1]]
            left_len = k - j + 1
            node.left = helper(i+1, j, left_len)
            node.right = helper(i+1+left_len, j+left_len, n - 1 - left_len)
            return node
        return helper(0, 0, len(pre))