#first create a Node Each Node should have data field and a reference field.
class Node(object):
	
	def __init__(self,data):
		self._data = data
		self.NextNode = None

class LinkedList(object):
	
	def __init__(self):
		self._head = None  # the head is always the root node, like tree we cannot have index to reach a particular value or location
		self._count =0

		#O(1) time complexity insertion
	def InsertStart(self,data):
		self._count = self._count + 1
		newNode = Node(data)
		if not self._head:
			self._head = newNode
		else:
			newNode.NextNode = self._head
			self._head = newNode

	#O(1) since 		
	def size(self):
		return self._count

	def size2(self):
		total = 0
		tempList = self._head
		while tempList:
			total  = total + 1
			tempList = tempList.NextNode
		return total

if __name__ == '__main__':
	myLL = LinkedList()
	myLL.InsertStart(10)
	myLL.InsertStart(20)
	myLL.InsertStart(30)
	print myLL.size2()
	print myLL.size()