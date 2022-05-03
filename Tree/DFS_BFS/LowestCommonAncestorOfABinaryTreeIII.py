class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

# It's the same as find join node of two linked lists
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        first = p
        second = q
        while first != second:
            first = first.parent if first.parent else q
            second = second.parent if second.parent else p
        return first

