# Deal collision by Array
from tkinter import W


class MyHashMap:
    def __init__(self):
        self.capacity = 1000
        self.records = [[] for _ in range(self.capacity)]
        return

    def encode(self, key):
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        code = self.encode(key)
        if not self.records[code]:
            self.records[code].append((key, value))
        else:
            for i in range(len(self.records[code])):
                if self.records[code][i][0] == key:
                    self.records[code][i] = (key, value)
                    return
            self.records[code].append((key, value))

    def get(self, key: int) -> int:
        code = self.encode(key)
        if not self.records[code]:
            return -1
        else:
            for i in range(len(self.records[code])):
                if self.records[code][i][0] == key:
                    return self.records[code][i][1]
            return -1

    def remove(self, key: int) -> None:
        code = self.encode(key)
        for i in range(len(self.records[code])):
            if self.records[code][i][0] == key:
                self.records[code].remove(self.records[code][i])
                break

# Deal collision by LinkedList
class ListNode:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def empty(self):
        return self.length == 0

    def get(self, key) -> int:
        cur = self.head.next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def add(self, key, val: int) -> None:
        node = ListNode(key, val)
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        self.length += 1

    def upsert(self, key, val):
        cur = self.head.next
        while cur:
            if cur.key == key:
                cur.val = val
                return
            cur = cur.next
        self.add(key, val)

    def _delete(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def delete(self, key):
        cur = self.head.next
        while cur:
            if cur.key == key:
                self._delete(cur)
                return
            cur = cur.next

class MyHashMap2:
    def __init__(self):
        self.capacity = 1000
        self.records = [LinkedList() for _ in range(self.capacity)]
        return

    def encode(self, key):
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        # print("put:", key, value)
        code = self.encode(key)
        if self.records[code].empty():
            self.records[code].add(key, value)
        else:
            self.records[code].upsert(key, value)

    def get(self, key: int) -> int:
        # print("get:", key)
        code = self.encode(key)
        if not self.records[code]:
            return -1
        else:
            return self.records[code].get(key)

    def remove(self, key: int) -> None:
        # print('remove:', key)
        code = self.encode(key)
        self.records[code].delete(key)

hash = MyHashMap2()
hash.put(10001, 1)
hash.put(100001, 2)
hash.put(1000001, 3)
print(hash.get(10001)) # 1
print(hash.get(100001)) # 2
print(hash.get(1000001)) # 3
hash.put(10001, 10)
print(hash.get(10001)) # 10
print(hash.get(10002)) # -1
hash.remove(10001)
print(hash.get(10001)) # -1
print(hash.get(100001)) # 2

