class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1

        n = self.dict[key]
        self._remove(n)
        self._add(n)

        return n.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self._remove(self.dict[key])

        n = Node(key, value)
        self._add(n)
        self.dict[key] = n
        if len(self.dict) > self.capacity: # add new key
            # remove tail node and it's key
            r = self.tail.prev
            self._remove(r)
            del self.dict[r.key]        
            
    def _add(self, n):
        self.head.next.prev = n
        n.next = self.head.next
        self.head.next = n
        n.prev = self.head
        
    def _remove(self, n):
        n.prev.next = n.next
        n.next.prev = n.prev