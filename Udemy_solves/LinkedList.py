#first create a Node Each Node should have data field and a reference field.
class Node(object):
	
	def __init__(self,data):
		self._data = data
		self._NextNode = None

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
			newNode._NextNode = self._head
			self._head = newNode

	#O(1) since 		
	def size(self):
		return self._count

	#O(N) since we have to traverse all the way to the end
	def size2(self):
		total = 0
		tempLL = self._head
		while tempLL:
			total  = total + 1
			tempLL = tempLL._NextNode
		return total
	#O(N) complexity since we have to traverse all the way to the end of the LinkedList to insert the data
	def InsertEnd(self,data):
		self._count = self._count + 1
		newNode = Node(data)
		tempLL = self._head
		while tempLL._NextNode:
			tempLL = tempLL._NextNode
		tempLL._NextNode = newNode
		#self._head = tempLL

	def __str__(self):
		tempLL = self._head
		ll =[]
		while tempLL:
			ll.append(tempLL._data)
			tempLL = tempLL._NextNode
		return str(ll)

if __name__ == '__main__':
	myLL = LinkedList()
	myLL.InsertStart(10)
	myLL.InsertStart(20)
	myLL.InsertStart(30)
	print myLL.size2()
	print myLL.size()
	myLL.InsertEnd(25)
	print myLL
	print myLL.size()
	myLL.InsertStart(35)
	print myLL
	print myLL.size()