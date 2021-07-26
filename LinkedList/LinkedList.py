class ListNode:
	def __init__(self, val = None):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def add(self, value):
		node = ListNode(value)
		if (not self.head):
			self.head = node
		else:
			node.next = self.head
			self.head = node

	def remove(self):
		if (not self.head):
			print("list is empty")
		else:
			self.head = self.head.next

	def print(self):
		cur = self.head
		while(cur != None):
			print(cur.val)
			cur = cur.next

linked_list = LinkedList()
linked_list.add(1)
linked_list.add(3)
linked_list.add(5)
linked_list.add(7)
linked_list.remove()
linked_list.print() # 5,3,1
linked_list.remove()
linked_list.remove()
linked_list.print() # 1
linked_list.remove()
linked_list.print() # (empty)
linked_list.remove() # list is empty (do nothing)

