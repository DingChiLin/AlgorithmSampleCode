from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        que = deque([root])
        while que:
            ans.append([n.val for n in que])

            size = len(que)
            for _ in range(size):
                n = que.popleft()
                if n.left:
                    que.append(n.left)
                if n.right:
                    que.append(n.right)
        return ans

