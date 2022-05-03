class AVLTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

#  not allow duplicated value
class AVLTree:
    def __init__(self):
        self.root = None
    
    def _update_height(self, node):
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

    def _rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        self._update_height(node)
        self._update_height(right_child)
        return right_child

    def _rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        self._update_height(node)
        self._update_height(left_child)
        return left_child

    def _get_balance_factor(self, node):
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_height(self, node):
        return node.height if node else 0

    def _balance(self, node):
        bf = self._get_balance_factor(node)
        if (bf > 1 and self._get_balance_factor(node.left) >= 0): # LL
            return self._rotate_right(node)
        elif (bf > 1 and self._get_balance_factor(node.left) < 0): # LR
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        elif (bf < -1 and self._get_balance_factor(node.right) <= 0): # RR
            return self._rotate_left(node)
        elif (bf < -1 and self._get_balance_factor(node.right) > 0): # RL
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        else:
            return node

    def _insert(self, node, val):
        if (not node):
            return AVLTreeNode(val)
        else:
            if (val > node.val):
                node.right = self._insert(node.right, val)
            elif (val < node.val):                
                node.left = self._insert(node.left, val)
            else:
                return node # not allow duplicated value

            self._update_height(node)
            node = self._balance(node)
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

        res_node = None
        if (target > node.val):
            node.right = self._delete(node.right, target)
            res_node = node
        elif (target < node.val):
            node.left = self._delete(node.left, target)
            res_node = node
        else:
            if not node.left:
                res_node = node.right
            elif not node.right:
                res_node = node.left
            else:
                next_node = self._next(node)
                next_node.right = self._delete(node.right, next_node.val)
                next_node.left = node.left
                res_node = next_node
        
        if (not res_node):
            return None
        self._update_height(res_node)
        self._balance(res_node)
        return res_node

    def delete(self, val):
        self.root = self._delete(self.root, val)

    # in order traversal
    def _print(self, node):
        if (not node):
            return
        self._print(node.left)
        print(node.val, node.height)
        self._print(node.right)

    def print(self):
        self._print(self.root)


tree = AVLTree()

print("=== insert test ===")
tree.insert(7)
tree.insert(6)
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(2)
tree.insert(1)
tree.insert(3) # won't be inserted since it already existed
tree.print()

print("=== delete test ===")
tree.delete(1)
tree.delete(6)
tree.delete(4)
tree.insert(1)
tree.print()

print("=== random test ====")
import random
inserts = []
for i in range(1, 1000):
    n = random.randint(1,1000)
    inserts.append(n)
# inserts = list(set(inserts))
for n in inserts:
    tree.insert(n)

deletes = []
for i in range(1, 800):
    n = random.randint(1,1000)
    deletes.append(n)
# deletes = list(set(deletes))
for n in deletes:
    tree.delete(n)

tree.print()