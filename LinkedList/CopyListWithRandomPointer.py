from collections import defaultdict

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# space O(N)
class Solution:
    def __init__(self):
        self.visited = defaultdict(Node)
        
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        if head in self.visited:
            return self.visited[head]
        node = Node(head.val)
        self.visited[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node


# space O(1)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        original_cur = head

        # first pass
        while original_cur:
            original_next = original_cur.next
            copy = Node(original_cur.val)
            original_cur.next = copy
            copy.next = original_next
            original_cur = original_next


        # second pass
        original_cur = head
        while original_cur:
            if original_cur.random:
                original_cur.next.random = original_cur.random.next
            original_cur = original_cur.next.next

        copy_head = head.next

        # third pass
        cur = head
        while cur and cur.next:
            nxt = cur.next # copied node
            cur.next = cur.next.next
            cur = nxt

        return copy_head
