class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# 一般的 BFS，會用到額外記憶體空間
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        que = deque([(root, 0)])
        
        while que:
            node, level = que.popleft()
            if not que or level != que[0][1]:
                node.next = None
            else:
                node.next = que[0][0]
            if node.left:
                que.append((node.left, level + 1))
            if node.right:
                que.append((node.right, level + 1))
        
        return root

# DFS 做法，不會用到額外空間，但仍然會因為遞迴產生的 function stack 用到空間（題目敘述可接受）
class Solution:
    def connect2(self, n1, n2):
        n1.next = n2
        if (n1.right and n2.left):
            self.connect2(n1.right, n2.left)

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        if root.left and root.right:
            root.left.next = root.right
            if (root.left.right and root.right.left):
                self.connect2(root.left.right, root.right.left)
            self.connect(root.left)
            self.connect(root.right)
        return root

# 更聰明的 BFS 做法，完全不會用到額外空間（這題最完美的解法）
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        node = root
        while node and node.left:
            nextLevel = node.left
            # 利用這層的 next 指標，從左到右橫向掃過，處理好下一層的連結
            while node:
                node.left.next = node.right
                node.right.next = node.next.left if node.next else None
                node = node.next
            # 走向下一層
            node = nextLevel
        return root