#this AVL implementation is based on the Udemy lectures.
class Node(object):

	def __init__(self,data):
		self._data = data
		self.leftChild = None
		self.rightChild = None
		self._height = 0

class AVL(object):
	
	def __init__(self):
		self._root = None

	def _calculateHeight(self,node):
		if not node:
			return -1

		return node._height

	#If the balance is > 1 then it is a left heavy situation
	#If the balance is < -1 then it is a right heavy situation
	def _calculateBalance(self,node):

		if not node:
			return 0 #have to check 

		return self._calculateHeight(node.leftChild) - self._calculateHeight(node.rightChild)

	def _rotateRight(self,node):
		TempLeftchild = node.leftChild
		t = TempLeftchild.rightChild
		TempLeftchild.rightChild = node
		node.leftChild = t

		#Updating heights node update first
		node._height = max(self._calculateHeight(node.leftChild),self._calculateHeight(node.rightChild)) + 1
		TempLeftchild._height = max(self._calculateHeight(TempLeftchild.leftChild),self._calculateHeight(TempLeftchild.rightChild)) +1

		return TempLeftchild

	def _rotateLeft(self,node):
		tempRightchild = node.rightChild
		t = tempRightchild.leftChild
		tempRightchild.leftChild = node
		node.rightChild= t

		#Updating heights node update first
		node._height = max(self._calculateHeight(node.leftChild),self._calculateHeight(node.rightChild)) + 1
		tempRightchild._height = max(self._calculateHeight(tempRightchild.leftChild),self._calculateHeight(tempRightchild.rightChild)) +1

		return tempRightchild

	def insert(self,value):
		#if not self._root:
		#	self._root = Node(value)
		#else:
		self._root = self.insertValue(self._root,value)


	def insertValue(self,node,value): 

		if not node:
			return Node(value)

		if value < node._data:
			node.leftChild = self.insertValue(node.leftChild,value)

		else:
			node.rightChild = self.insertValue(node.rightChild,value)

		node._height = max(self._calculateHeight(node.leftChild),self._calculateHeight(node.rightChild)) + 1

		return self._validation(node,value)

	def _validation(self,node,value):
		balanace = self._calculateBalance(node)

		if balanace > 1 and value < node.leftChild._data:
			print 'left left heavy!'
			return self._rotateRight(node)

		if balanace < -1 and value > node.rightChild._data:
			print 'right right heavy!'
			return self._rotateLeft(node)

		if balanace > 1 and value > node.leftChild._data:
			print 'left right heavy!'
			node.leftChild = self._rotateLeft(node.leftChild)

			return self._rotateRight(node)

		if balanace < -1 and value < node.rightChild._data:
			print 'right left heavy!'
			#test

			#test
			node.rightChild = self._rotateRight(node.rightChild)
			
			return self._rotateLeft(node)

		return node

	def Trav(self):
		if self._root:
			self._travel(self._root)

	def _travel(self,node):
		if node.leftChild:
			self._travel(node.leftChild)

		print node._data

		if node.rightChild:
			self._travel(node.rightChild)

	def remove(self,value):
		if self._root:
			self._root = self._removeValue(self._root,value)


	def _getPredecessor(self,node):
		if node.rightChild:
			return self._getPredecessor(node.rightChild)

		return node

	def _removeValue(self,node,value):
		if not node:
			return node

		if value< node._data:
			node.leftChild = self._removeValue(node.leftChild,value)

		elif value > node._data:
			node.rightChild = self._removeValue(node.rightChild,value)

		else:
			if not node.rightChild and not node.leftChild:
				del node
				node  = None
				return node

			if not node.leftChild:
				tempnode =  node.rightChild
				del node
				node = None
				return tempnode

			if not node.rightChild:
				tempnode =  node.leftChild
				del node
				node = None
				return tempnode

			tempnode = self._getPredecessor(node.leftChild)
			node._data = tempnode._data
			node.leftChild = self._removeValue(node.leftChild,tempnode._data)

		node._height = max(self._calculateHeight(node.leftChild),self._calculateHeight(node.rightChild)) + 1
		balance  = self._calculateBalance(node)

		if balance > 1 and self._calculateBalance(node.leftChild) >=0:
			#left heavy
			return self._rotateRight(node)

		if balance > 1 and self._calculateBalance(node.leftChild) < 0:
			#left right
			self.node.leftChild = self._rotateLeft(node.leftChild)
			return self._rotateRight(node)

		if balance < -1 and self._calculateBalance(node.rightChild) <=0:
			#right heavy
			return self._rotateLeft(node)

		if balance < -1 and self._calculateBalance(node.rightChild) > 0:
			#right left
			self.node.rightChild = self._rotateRight(node.rightChild)
			return self._rotateLeft(node)

		return node






if __name__ == '__main__':
	mytree = AVL()
	mytree.insert(50)
	mytree.insert(40)
	mytree.insert(45)
	mytree.insert(20)
	mytree.insert(30)
	mytree.insert(60)
	mytree.insert(9)
	mytree.insert(8)
	mytree.insert(7)
	mytree.insert(11)
	mytree.insert(1)
	mytree.Trav()
	print '--------'
	mytree.remove(100)
	mytree.Trav()
	print '--------'
	mytree.remove(45)
	mytree.remove(20)
	mytree.remove(30)
	mytree.insert(11)
	mytree.Trav()