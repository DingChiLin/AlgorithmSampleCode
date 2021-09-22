# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, x = None):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        res = []
        def dfs(node):
            if node:
                res.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                res.append('*')

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(',')
        self.index = 0
        def dfs():
            val = vals[self.index]
            self.index += 1
            if val != '*':
                node = TreeNode(int(val))
                node.left = dfs()
                node.right = dfs()
                return node
            else:
                return None
        return dfs()

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()

root = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.left = node5

print(ser.serialize(root))
root2 = deser.deserialize(ser.serialize(root))

def dfs(node):
    if not node:
        return
    print(node.val)
    dfs(node.left)
    dfs(node.right)
dfs(root)
dfs(root2)