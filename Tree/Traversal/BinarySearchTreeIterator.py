from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.current = root 
        while self.current:
            self.stack.append(self.current)
            self.current = self.current.left

    def next(self) -> int:
        self.current = self.stack.pop()
        val = self.current.val
        self.current = self.current.right
        while self.current:
            self.stack.append(self.current)
            self.current = self.current.left
        return val
                      
    def hasNext(self) -> bool:
        return len(self.stack) > 0
