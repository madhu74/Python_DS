#first create a Node Each Node should have data field and a reference field.
class Node(object):
	
	def __init__(self,data):
		self._data = data
		self._NextNode = None #Reference

class LinkedList(object):
	
	def __init__(self):
		self._head = None  # the head is always the root node (reference to the first node), like tree we cannot have index to reach a particular value or location
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
	def __len__(self):
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

	def remove_buggy(self,data): #Need to test
		if self._head is None:
			return
		previousNode = None
		currentNode  = self._head

		while currentNode._data != data:
			previousNode = currentNode
			currentNode = currentNode._NextNode

		if previousNode is None:
			self._count = self._count - 1
			self._head = currentNode._NextNode
			
		else:
			self._count = self._count - 1
			previousNode._NextNode = currentNode._NextNode

	#O(N) complexity since we have to traverse to find the data
	def deleteNode(self,data): #this should work
		temp = self._head
		if temp is None:
			return

		if temp is not None:
			if temp._data == data:
				self._head = temp._NextNode
				temp = None
				self._count = self._count -1
				return

		while temp is not None:
			if temp._data == data:
				break
			previousNode = temp
			temp = temp._NextNode

		if temp is None:
			return
		
		previousNode._NextNode = temp._NextNode
		self._count = self._count -1
		temp =None



	def __str__(self):
		tempLL = self._head
		ll =[]
		while tempLL:
			ll.append(tempLL._data)
			#print tempLL,tempLL._NextNode
			tempLL = tempLL._NextNode
		return str(ll)

if __name__ == '__main__':
	myLL = LinkedList()
	myLL.InsertStart(10)
	myLL.InsertStart(20)
	myLL.InsertStart(30)
	print myLL.size2()
	print len(myLL)
	myLL.InsertEnd(25)
	print myLL
	#print len(myLL)
	myLL.InsertStart(35)
	print myLL
	print len(myLL)
	myLL.deleteNode(30)
	print myLL
	print len(myLL)