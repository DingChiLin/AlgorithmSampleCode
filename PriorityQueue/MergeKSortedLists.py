from typing import List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = []
        for i in range(len(lists)):
            n = lists[i]
            if n:
                heapq.heappush(q, (n.val, i))
                lists[i] = n.next

        root = ListNode(None)
        cur = root
        while q:
            (val, i) = heapq.heappop(q)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i]:
                heapq.heappush(q, (lists[i].val ,i))
                lists[i] = lists[i].next

        return root.next