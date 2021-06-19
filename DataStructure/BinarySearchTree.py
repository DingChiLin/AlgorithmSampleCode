class BSTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# binary search tree without self-balancing
class BSTree:
    def __init__(self):
        self.root = None

    def _insert(self, node, val):
        if (not node):
            return BSTreeNode(val)
        else:
            if (val >= node.val):
                node.right = self._insert(node.right, val)
            else:                
                node.left = self._insert(node.left, val)
            return node

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _next(self, node):
        if (not node):
            return None
        if (not node.right):
            return None
        cur_node = node.right
        while cur_node.left:
            cur_node = cur_node.left
        return cur_node

    def _delete(self, node, target):
        if (not node):
            return None

        if (target > node.val):
            node.right = self._delete(node.right, target)
            return node
        elif (target < node.val):
            node.left = self._delete(node.left, target)
            return node
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                next_node = self._next(node)
                next_node.right = self._delete(node.right, next_node.val)
                next_node.left = node.left
                return next_node

    def delete(self, val):
        self.root = self._delete(self.root, val)

    # in order traversal
    def _print(self, node):
        if (not node):
            return
        self._print(node.left)
        print(node.val)
        self._print(node.right)

    def print(self):
        self._print(self.root)

tree = BSTree()

print("=== insert test ===")
tree.insert(4)
tree.insert(2)
tree.insert(6)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(7)
tree.print()

print("=== delete test ===")
tree.delete(1)
tree.delete(6)
tree.delete(4)
tree.print()

print("=== random test ====")
import random
for i in range(1, 100):
    tree.insert(random.randint(1,100))
for i in range(1, 200):
    tree.delete(random.randint(1,100))
tree.print()