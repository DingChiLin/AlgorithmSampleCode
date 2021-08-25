# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def concat(self, node1, node2, carry = 0):
        n1 = 0 if not node1 else node1.val
        n2 = 0 if not node2 else node2.val
        tot = n1 + n2 + carry
        val = tot % 10
        carry = tot // 10

        node = ListNode(val)
        next1 = None if not node1 else node1.next
        next2 = None if not node2 else node2.next
        if next1 or next2 or carry:
            node.next = self.concat(next1, next2, carry)
        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.concat(l1, l2, 0)