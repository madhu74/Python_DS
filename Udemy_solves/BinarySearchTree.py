#this implementation is based on Udemy lectures.
class Node(object):

	def __init__(self,data):
		self._data = data
		self._leftChild = None
		self._rightChild = None

class BinarySearchTree(object):
	
	def __init__(self):
		self._root = None

	def insert(self,data):
		if not self._root:
			self._root = Node(data)
		else:
			self._insertValue(data,self._root)

	def _insertValue(self,data,node):
		if data < node._data:
			if node._leftChild:
				self._insertValue(data,node._leftChild)

			else:
				node._leftChild = Node(data)

		else:
			if node._rightChild:
				self._insertValue(data,node._rightChild)

			else:
				node._rightChild = Node(data)

	def travresal(self):
		if self._root:
			return self._Trav(self._root)

	def _Trav(self,node):
		if node._leftChild:
			self._Trav(node._leftChild)

		print node._data

		if node._rightChild:
			self._Trav(node._rightChild)


	def remove(self,data):
		if self._root:
			self._root = self._removeValue(data,self._root)

	def _removeValue(self,data,node):

		if not node:
			return node

		if data < node._data:
			node._leftChild = self._removeValue(data,node._leftChild)  #we have to update the reference manually once the value have been deleted
			#We have to tell the parent that this node has been updated. since we are travelling through references

		elif data > node._data:
			node._rightChild = self._removeValue(data,node._rightChild) #we have to update the reference manually once the value have been deleted

		else:
			if not node._rightChild and not node._leftChild:
				del node
				return None

			if not node._rightChild:
				temp = node._leftChild
				del node
				node = None
				return temp

			elif not node._leftChild:
				temp = node._rightChild
				del node
				node = None
				return temp

			temp = self._getPredecessor(node._leftChild)
			node._data = temp._data
			node._leftChild = self._removeValue(temp._data, node._leftChild)

		return node

	def _getPredecessor(self,node):

		if node._rightChild:
			return self._getPredecessor(node._rightChild)
			
		return node


if __name__ =='__main__':
	Mybst  = BinarySearchTree()
	Mybst.insert(10)
	Mybst.insert(5)
	Mybst.insert(15)
	Mybst.insert(7)
	Mybst.insert(4)
	Mybst.insert(16)
	Mybst.insert(14)
	Mybst.travresal()
	Mybst.remove(10)
	Mybst.travresal()