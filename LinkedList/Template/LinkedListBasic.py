'''
最基礎初學者要會的部分：
1. Single Linked List
2. 給予 self.head 一個空的 Node
3. 記錄 length
'''

class ListNode:
	def __init__(self, val = None):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = ListNode()
		self.length = 0

	def add(self, value): # add at head
		node = ListNode(value)
		node.next = self.head.next
		self.head.next = node
		self.length += 1

	def remove(self): # remove at head
		if self.head.next:
			self.head.next = self.head.next.next
			self.length -= 1
		else:
			print("list is empty")

	def print(self):
		cur = self.head.next
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
linked_list.remove() # list is empty

