class Empty(Exception):
	pass

class Queue1(object):
	CONSTANT_LENGTH = 10
	
	def __init__(self):
		self._data =[None]*Queue1.CONSTANT_LENGTH
		self._front = 0
		self._size = 0

	def __len__(self):
		return self._size

	def isEmpty(self):
		return self._size == 0

	def first(self):
		if self.isEmpty():
			raise Empty('Queue is empty')
		return self._data[self._front]

	def dequeue(self):
		""" we allow the front of the queue to drift rightward, and we allow the contents of the 
		queue to 'wrap around' the end of an underlying array (Using an Array Circularly) page 242"""
		if self.isEmpty():
			raise Empty('Queue is empty')

		if 0 < self._size < (len(self._data)//4):  #reducing the size of the queue
			self.resize((len(self._data)//2))

		answer = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front+1) % len(self._data) # using arrays circularly 
		self._size = self._size - 1
		return answer

	def enqueue(self,value):
		""" We need to determine the proper index at which to place the new element. Although
		we do not explicitly maintain an instance variable for the back of the queue, we
		compute the location of the next opening based on the formula: avail = (self. front + self. size) % len(self. data) """
		if self._size == len(self._data):
			self.resize(self._size*2)
		insert_index = (self._front + self._size) % len(self._data)
		self._data[insert_index] = value
		self._size = self._size + 1


	def resize(self,mag):
		old = self._data
		self._data = [None]*mag
		k = self._front
		for i in range(self._size):
			self._data[i] = old[k]
			k= (k+1) % len(old) # traversing arrays circularly 
		self._front = 0


class Queue2(object):
	""" This implementation is based on Udemy, this have many drawbacks like insert(index,value) have time complexity O(n), but above
	implementation have time complexity O(1)"""
	def __init__(self):
		self._data =[]

	def __len__(self):
		return len(self._data)

	def first(self):
		return self._data[-1]

	def enqueue(self,value):
		self._data.insert(0,value)

	def dequeue(self):
		return self._data.pop()


if __name__ == '__main__':
	firstq = Queue1()
	print firstq.isEmpty()
	for i in xrange(1,13):
		firstq.enqueue(i)
	print firstq.first()
	print firstq.dequeue()
	print firstq.dequeue()
	print firstq.dequeue()
	print firstq.dequeue()
	print firstq.dequeue()
	print firstq.dequeue()
	print firstq.dequeue()
	print firstq.dequeue()
	print firstq.dequeue()
	print firstq.dequeue()
	print firstq.dequeue()
	firstq.enqueue(12)
	print firstq.first()
	print len(firstq)
	
	print '##########################################type2##################################'
	
	twoq = Queue2()
	for i in xrange(1,13):
		twoq.enqueue(i)
	print twoq.first()
	print twoq.dequeue()
	print twoq.dequeue()
	print twoq.dequeue()
	print twoq.dequeue()
	print twoq.dequeue()
	print twoq.dequeue()
	print twoq.dequeue()
	print twoq.dequeue()
	print twoq.dequeue()
	print twoq.dequeue()
	print twoq.dequeue()
	twoq.enqueue(12)
	print twoq.first()
	print len(twoq)