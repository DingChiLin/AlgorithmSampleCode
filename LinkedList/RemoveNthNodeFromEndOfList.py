from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def remove(self, node, target):
        if not node:
            return 1
        depth = self.remove(node.next, target)
        if depth == target + 1:
            node.next = node.next.next
        return depth + 1
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0) # add an dummy node at top for convenience
        dummy.next = head
        self.remove(dummy, n)
        return dummy.next

head = ListNode(0)
node = head
for n in [1,4,3,2,5,2]:
    node.next = ListNode(n)
    node = node.next
head = head.next

s = Solution()
r = s.removeNthFromEnd(head, 5)
while r:
    print(r.val)
    r = r.next