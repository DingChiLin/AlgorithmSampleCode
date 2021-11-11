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

    def getPredecessor(self, node):
        pred = node.left
        while pred.right:
            pred = pred.right
        return pred

    def _delete(self, node, target):
        if not node:
            return None
        elif target > node.val:
            node.right = self._delete(node.right, target)
        elif target < node.val:
            node.left = self._delete(node.left, target)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                pred = self.getPredecessor(node)
                node.val = pred.val
                node.left = self._delete(node.left, pred.val)
        return node

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _exist(self, node, val):
        if not node:
            return False
        if val == node.val:
            return True
        elif val > node.val:
            return self._exist(node.right, val)
        else:
            return self._exist(node.left, val)

    def exist(self, val):
        return self._exist(self.root, val)

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
tree.print() # 1 2 3 4 5 6 7
print(tree.exist(1)) # True
print(tree.exist(4)) # True
print(tree.exist(8)) # False

print("=== delete test ===")
tree.delete(1)
tree.delete(6)
tree.delete(4)
tree.print() # 2 3 5 7
print(tree.exist(1)) # False
print(tree.exist(4)) # False
print(tree.exist(8)) # False

# print("=== random test ====")
# import random
# for i in range(1, 100):
#     tree.insert(random.randint(1,100))
# for i in range(1, 200):
#     tree.delete(random.randint(1,100))
# tree.print()