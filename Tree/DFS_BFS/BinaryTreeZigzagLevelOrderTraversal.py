from typing import List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []

        result = []
        queue = deque()
        queue.append(root)

        level = 0
        while queue:
            values = []
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2 == 1:
                values = values[::-1] # reverse
            result.append(values)
            level += 1

        return result