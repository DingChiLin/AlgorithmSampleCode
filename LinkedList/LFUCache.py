from collections import defaultdict

class ListNode:
    def __init__(self, key = None, val = None, freq = None):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val
        self.freq = freq

class DoubleLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    # add front
    def add(self, node): 
        node.next = self.head.next
        self.head.next.prev = node 
        node.prev = self.head
        self.head.next = node
        self.length += 1

    # pop back
    def pop(self):
        if self.empty():
            return
        node = self.tail.prev
        self.remove(node)
        return node
    
    # remove in the middle
    def remove(self, node):
        node.next.prev, node.prev.next = node.prev, node.next
        self.length -= 1

    def empty(self):
        return self.length == 0

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_cnt = 0
        self.min_freq = 1
        self.table = {} # {key: ListNode}
        self.freq_nodes = defaultdict(DoubleLinkedList) # {freq: DoubleLinkedList}

    def visit(self, node: ListNode):
        self.freq_nodes[node.freq].remove(node)
        if self.freq_nodes[self.min_freq].empty():
            self.min_freq += 1
        node.freq += 1
        self.freq_nodes[node.freq].add(node)

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1
        if key in self.table:
            node = self.table[key]
            self.visit(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.table:
            node = self.table[key]
            node.val = value
            self.visit(node)
        else:
            if self.node_cnt == self.capacity:
                popped_node = self.freq_nodes[self.min_freq].pop()
                del self.table[popped_node.key]
                self.node_cnt -= 1

            self.min_freq = 1
            node = ListNode(key, value, self.min_freq)            
            self.freq_nodes[node.freq].add(node)
            self.table[node.key] = node
            self.node_cnt += 1
