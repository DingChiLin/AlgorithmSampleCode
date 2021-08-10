'''
完整的 Double Linked List (Leetcode 707)
'''

class ListNode:
    def __init__(self, val = None):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def _insertBehindTarget(self, target, val):
        node = ListNode(val)
        target.prev.next = node
        node.prev = target.prev
        target.prev = node
        node.next = target
        self.length += 1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self._insertBehindTarget(self.tail, val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return None

        cur = self.head.next
        for _ in range(index):
            cur = cur.next

        self._insertBehindTarget(cur, val)

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return None

        cur = self.head.next
        for _ in range(index):
            cur = cur.next

        cur.next.prev = cur.prev
        cur.prev.next = cur.next
        self.length -= 1

obj = MyLinkedList()
obj.addAtHead(1) # [1]
print(obj.get(0)) # 1
obj.addAtHead(2) # [2, 1]
print(obj.get(1)) # 1
print(obj.get(2)) # -1
obj.addAtTail(3) # [2, 1, 3]
print(obj.get(2)) # 3
obj.deleteAtIndex(1) # [2, 3]
print(obj.get(1)) # 3
obj.deleteAtIndex(2) # (do nothing)
print(obj.get(1)) # 3