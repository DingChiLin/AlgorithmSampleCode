class ListNode:
    def __init__(self, key = None, val = None, freq = None):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val
        self.freq = freq

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cnt = 0
        self.min_freq = 1
        self.table = {} # {key: node}
        self.freq_nodes = {} # {freq: (head node, tail node)}

    def add(self, node: ListNode):
        if (node.freq not in self.freq_nodes):
            head = ListNode()
            tail = ListNode()
            head.next = tail
            tail.prev = head
            self.freq_nodes[node.freq] = (head, tail)
        self.table[node.key] = node
        head = self.freq_nodes[node.freq][0]
        nxt = head.next
        head.next = node
        node.next = nxt
        nxt.prev = node
        node.prev = head

    def remove(self, node: ListNode):
        del self.table[node.key]
        prv = node.prev
        nxt = node.next
        prv.next = nxt
        nxt.prev = prv

    def visit(self, node: ListNode):
        self.remove(node)
        # list is empty
        if (self.freq_nodes[node.freq][0].next == self.freq_nodes[node.freq][1] and node.freq == self.min_freq):
            self.min_freq += 1
        node.freq += 1
        self.add(node)

    def get(self, key: int) -> int:
        if (self.capacity == 0):
            return -1
        if (key in self.table):
            self.visit(self.table[key])
            return self.table[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if (self.capacity == 0):
            return
        if (key in self.table):
            self.table[key].val = value
            self.visit(self.table[key])
        else:
            if self.cnt == self.capacity:
                tail = self.freq_nodes[self.min_freq][1]
                target_node = tail.prev
                self.remove(target_node)
                self.cnt -= 1
            
            self.min_freq = 1
            node = ListNode(key, value, self.min_freq)
            self.add(node)
            self.cnt += 1

        return 0
