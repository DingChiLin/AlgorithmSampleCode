class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def cutInMiddle(self, head):
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        return head, slow
 
    def merge(self, left, right):
        root = ListNode(None)
        n = root

        while left and right:
            if left.val < right.val:
                n.next = left
                left = left.next
            else:
                n.next = right
                right = right.next
            n = n.next

        if left:
            n.next = left
        if right:
            n.next = right

        return root.next

    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        # cut in middle
        left, right = self.cutInMiddle(head)

        # sort each half
        left = self.sortList(left)
        right = self.sortList(right)

        # merge
        return self.merge(left, right)
