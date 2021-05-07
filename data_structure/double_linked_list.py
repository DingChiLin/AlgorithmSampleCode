class ListNode:
	def __init__(self, key = None, val = None):
		self.key = key
		self.val = val
		self.next = None
		self.prev = None

class DoubleLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def append_left(self, key, val):
		node = ListNode(key, val)
		if (self.head == None):
			self.head = node
			self.tail = node
		else:
			node.next = self.head
			self.head.prev = node
			self.head = node

	def append_right(self, key, val):
		node = ListNode(key, val)
		if (self.head == None):
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			node.prev = self.tail
			self.tail = node

	def find(self, key):
		cur = self.head
		while(cur):
			if cur.key == key:
				return cur
			cur = cur.next
		return None

	def remove(self, node):
		if not node:
			return
		if not node.prev:
			self.head = node.next
		else:
			node.prev.next = node.next
		if not node.next:
			self.tail = node.prev
		else:
			node.next.prev = node.prev

	def print(self):
		cur = self.head
		while(cur != None):
			print(cur.val)
			cur = cur.next

linked_list = DoubleLinkedList()
linked_list.print() # empty
linked_list.append_left(1,'a')
linked_list.append_left(2,'b')
linked_list.append_right(3,'c')
linked_list.append_right(4,'d')
linked_list.print() # b, a, c, d

node1 = linked_list.find(1)
linked_list.remove(node1)
node3 = linked_list.find(3)
linked_list.remove(node3)
linked_list.print() # b, d

