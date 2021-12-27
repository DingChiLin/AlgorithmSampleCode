from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iteratively
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt   
        return prev

# Recursively
class Solution:
    def helper(self, prev, curr):
        if curr is None:
            return prev
        
        nxt = curr.next
        curr.next = prev
        
        return self.helper(curr, nxt)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(None, head)