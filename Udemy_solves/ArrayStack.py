class Empty(Exception):
	''' This is a small subclass for python exception'''
	pass

'''The stack uses the concept of last-in-first-out(LIFO)'''
class ArrayStack(object):

	def __init__(self):
		self._data =[]
	
	def __len__(self): #this is used to find the size of the stack
		return len(self._data)

	def Push(self,element):
		''' Adds the element to the top of the stack'''
		self._data.append(element)

	def isEmpty(self):
		''' This is used to check if the stack is empty, returns True or False'''
		return len(self._data) == 0

	def Pop(self):
		'''Remove and return the first element from the top of the stack '''
		if self.isEmpty():
			raise Empty('Stack is empty')
		return self._data.pop()

	def Top(self):
		'''Return the first element from the top of the stack '''
		if self.isEmpty():
			raise Empty('Stack is empty')
		return self._data[-1]

if __name__ == '__main__':
	myStack = ArrayStack()
	myStack.Push(4)
	myStack.Push(5)
	myStack.Push(6)
	myStack.Push(7)
	print myStack.isEmpty()
	print myStack.Pop()
	print myStack.Pop()
	print myStack.Top()
	print myStack.Pop()
	print myStack.Pop()
	print myStack.isEmpty()
	print myStack.Pop()
	print myStack.Top()



