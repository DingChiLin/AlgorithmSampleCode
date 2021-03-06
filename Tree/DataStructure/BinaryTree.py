class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

'''
Tree:
     4
   2   6
  1 3 5 7  
'''

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

def DFS_recursion(root):
    def pre_order(node):
        if not node:
            return
        print(node.val, end = " ")
        pre_order(node.left)
        pre_order(node.right)

    def in_order(node):
        if not node:
            return
        in_order(node.left)
        print(node.val, end = " ")
        in_order(node.right)

    def post_order(node):
        if not node:
            return
        post_order(node.left)
        post_order(node.right)
        print(node.val, end = " ")

    def pre_order_with_depth(node, depth):
        if not node:
            return
        print((node.val, depth), end = " ")
        pre_order_with_depth(node.left, depth + 1)
        pre_order_with_depth(node.right, depth + 1)

    print("Pre order:", end = " ")
    pre_order(root) # 4, 2, 1, 3, 6, 5, 7
    print("\nIn order:", end = " ")
    in_order(root) # 1, 2, 3, 4, 5, 6, 7
    print("\nPost order:", end = " ")
    post_order(root) # 1, 3, 2, 5, 7, 6, 4
    print("\nPre order with depth:", end = " ")
    pre_order_with_depth(root, 1) # (4, 1) (2, 2) (1, 3) (3, 3) (6, 2) (5, 3) (7, 3)
    print("")

def DFS_iteration(root):
    def pre_order(root):
        if not root:
            return
        
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans

    def in_order(root):
        if not root:
            return

        ans = []
        current = root
        stack = []
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                ans.append(current.val)
                current = current.right
            else:
                break
        return ans

    def post_order(root):
        if not root:
            return

        ans = []
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            right = stack[-1].right
            if (right):
                curr = right
            else:
                node = stack.pop()
                while (stack and stack[-1].right == node):
                    ans.append(node.val)
                    node = stack.pop()
                ans.append(node.val)
        return ans

    # An easier way but has side effect (It will break the original tree)
    def post_order_2(root):
        if root is None:
            return

        ans = []
        stack = [root]
        while stack:
            node = stack[-1]
            if not node.left and not node.right:
                stack.pop()
                ans.append(node.val)

            if node.right:
                stack.append(node.right)
                node.right = None

            if node.left:
                stack.append(node.left)
                node.left = None
        return ans

    print("Pre order:", end = " ")
    print(pre_order(root)) # [4, 2, 1, 3, 6, 5, 7]
    print("In order:", end = " ")
    print(in_order(root)) # [1, 2, 3, 4, 5, 6, 7]
    print("Post order:", end = " ")
    print(post_order(root)) # [1, 3, 2, 5, 7, 6, 4]

from collections import deque
def BFS_iteration(root):
    queue = deque()
    queue.append(root)
    
    ans = []
    while queue:
        node = queue.popleft()
        ans.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    print(ans) # [4, 2, 6, 1, 3, 5, 7]

def BFS_iteration_with_depth(root):

    def bfs_with_depth_1(root):
        queue = deque()
        queue.append((root, 1))

        ans = []
        while queue:
            node, depth = queue.popleft()
            ans.append((node.val, depth))
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return ans

    def bfs_with_depth_2(root):
        queue = deque()
        queue.append(root)

        ans = []
        depth = 1
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                ans.append((node.val, depth))
                if node.left:
                    queue.append((node.left))
                if node.right:
                    queue.append((node.right))
            depth += 1
        return ans
    
    print(bfs_with_depth_1(root)) # [(4, 1), (2, 2), (6, 2), (1, 3), (3, 3), (5, 3), (7, 3)]
    print(bfs_with_depth_2(root)) # [(4, 1), (2, 2), (6, 2), (1, 3), (3, 3), (5, 3), (7, 3)]

print("===== DFS Recursion =====")
DFS_recursion(root)
print("")

print("===== DFS Iteration (By Stack) =====")
DFS_iteration(root)
print("")

print("===== BFS Iteration (By Queue) =====")
BFS_iteration(root)
print("")

print("===== BFS Iteration with Level (By Queue) =====")
BFS_iteration_with_depth(root)