#Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, array):
        if not array:
            self.root = None

        nodeValues = deque(array)
        self.root = TreeNode(nodeValues.popleft())
        queue = deque([self.root])

        while queue and nodeValues:
            node = queue.popleft()
            left = nodeValues.popleft() if len(nodeValues) > 0 else None
            right = nodeValues.popleft() if len(nodeValues) > 0 else None

            if left != None:
                node.left = TreeNode(int(left))
                queue.append(node.left)

            if right != None:
                node.right = TreeNode(int(right))
                queue.append(node.right)

    def getRoot(self):
        return self.root

    @staticmethod
    def depth(head):
        max_depth = 0
        stack = []
        stack.append((head, 1))
        while stack:
            (node, level) = stack.pop()
            max_depth = max(max_depth, level)

            if node.right:
                stack.append((node.right, level+1))
            if node.left:
                stack.append((node.left, level+1))

        return max_depth

    def pprint(head):
        if not head:
            print(None)
            return

        max_depth = Tree.depth(head)
        
        level_max_count = [2**i for i in range(max_depth)]
        level_count = [0 for i in range(max_depth)]
        
        queue = deque()
        queue.append((head, 1))
        while queue:
            (node, level) = queue.popleft()
            if level_count[level-1] == 0:
                for _ in range(int(2**(max_depth - level + 1) - 2)):
                    print(" ", end = "")
            else:
                for _ in range(int(2**(max_depth - level + 2) - 1)):
                    print(" ", end = "")

            value = " " if node.val == None else node.val
            print(value, end = "")

            level_count[level-1] += 1

            if level_count[level-1] == level_max_count[level-1]:
                print('')

            if level < max_depth:
                if node.left:
                    queue.append((node.left, level+1))
                else:
                    queue.append((TreeNode(None), level+1))
                if node.right:
                    queue.append((node.right, level+1))
                else:
                    queue.append((TreeNode(None), level+1))

root = Tree([1,2,3,None,4,None,5,6,7]).getRoot()
print(root.val) # 1
print(root.left.val) # 2

'''
              1
      2               3
          4               5
        6   7     
'''
Tree.pprint(root)