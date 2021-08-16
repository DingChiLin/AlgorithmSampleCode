'''
完整的 Singly Linked List (Leetcode 707)
'''

class ListNode:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return None

        cur = self.head
        for _ in range(index):
            cur = cur.next

        node = ListNode(val)
        node.next = cur.next
        cur.next = node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return None

        cur = self.head
        for _ in range(index):
            cur = cur.next

        cur.next = cur.next.next
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