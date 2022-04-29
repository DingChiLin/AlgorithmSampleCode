from typing import Optional
from math import inf
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def int2str(self, x):
        res = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        return ''.join(res[::-1])

    def str2int(self, s):
        result = 0
        for ch in s:
            result = result * 256 + ord(ch)
        return result

    def preorder(self, root):
        res = []
        def helper(node):
            if not node:
                return
            res.append(self.int2str(node.val))
            helper(node.left)
            helper(node.right)
        helper(root)
        return res

    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = self.preorder(root)
        return ''.join(arr)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        arr = deque()
        i = 0
        while i < len(data):
            arr.append(self.str2int(data[i:i+4]))
            i += 4

        def helper(left, right):
            if not arr:
                return
            if arr[0] < left or arr[0] > right:
                return
            val = arr.popleft()
            node = TreeNode(val)
            node.left = helper(left, val)
            node.right = helper(val, right)
            return node
        return helper(-inf, inf)