class Node(object):
	def __init__(self,val):
		self.value = val
		self.next = None

	def __str__(self):
		return str(self.value)

class LinkedList(object):
	def __init__(self,val=None):
		if val != None:
			self.head = Node(val)
			self.len = 1
		else:
			self.head = None
			self.len = 0

	def length(self):
		return self.len

	def addNode(self,val):
		last_node = self.head
		if self.head != None:
			while last_node.next != None:
				last_node = last_node.next
			last_node.next = Node(val)
			self.len += 1
		else:
			self.head = Node(val)
			self.len += 1

		
	def delNode(self,val):
		if self.head != None:
			# head
			next_node = self.head
			if next_node.value == val:
				self.head = next_node.next
				self.len -= 1
				return True
			# body
			prev_node = self.head
			next_node = next_node.next
			while next_node.next != None:
				if next_node.value == val:
					prev_node.next = next_node.next
					self.len -= 1
					return True
				prev_node = prev_node.next
				next_node = next_node.next
			# tail	
			if next_node.value == val:
				prev_node.next = None
				self.len -= 1
				return True
		return False

	def __str__(self):
		printable = ''
		next_node = self.head
		if self.head != None:
			while next_node.next != None:
				printable += str(next_node.value) + ','
				next_node = next_node.next
			printable += str(next_node.value)
		return printable
		
	def kthToLast(self,k):
		if k < self.len:
			l = LinkedList()
			next_node = self.head
			for _ in range(k):
				next_node = next_node.next
			while next_node.next != None:
				l.addNode(next_node.value)
				next_node = next_node.next
			l.addNode(next_node.value)
			return l
		return None
	

if __name__ == "__main__":
	l = LinkedList()
	for i in range(25,50):
		l.addNode(i)
	print l.kthToLast(1)


