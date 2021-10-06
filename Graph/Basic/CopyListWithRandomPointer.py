class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        self.visited = defaultdict(ListNode)
        
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        if head in self.visited:
            return self.visited[head]
        node = ListNode(head.val)
        self.visited[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node