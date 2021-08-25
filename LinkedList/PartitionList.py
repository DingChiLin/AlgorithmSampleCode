class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less = ListNode(0)
        ln = less
        greater = ListNode(0)
        gn = greater

        n = head
        while n:
            if n.val < x:
                ln.next = ListNode(n.val)
                ln = ln.next 
            else:
                gn.next = ListNode(n.val)
                gn = gn.next
            n = n.next
        ln.next = greater.next
        return less.next

head = ListNode(0)
node = head
for n in [1,4,3,2,5,2]:
    node.next = ListNode(n)
    node = node.next
head = head.next

s = Solution()
r = s.partition(head, 3)
while r:
    print(r.val)
    r = r.next