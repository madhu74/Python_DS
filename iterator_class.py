class SequenceIteratorT1(object):

	def __init__(self,sequence):
		self._seq = sequence 	#sequence
		self._k = -1 			#index

	"""def __len__(self):
		return len(self._seq)

	def __getitem__(self,index):
		return self._seq[index]"""

	def next(self):				#NOTE: it is next() not __next__(), __next__() should be used in python 3
		self._k += 1
		if self._k > len(self._seq): 
			raise StopIteration()
		else:
			return self._seq[self._k]

	def __iter__(self):
		return self

class SequenceIteratorT2(object):
	def __init__(self,sequence):
		self._seq = sequence 	#sequence
		self._k = -1 			#index

	def __len__(self):
		return len(self._seq)

	def __getitem__(self,index):
		return self._seq[index]

	def __str__(self):
		return "<" + str(self._seq[:]) + ">"

""" If we have __len__(),__getitem__() we get default implementation of __iter__(),__next()__ and even __reversed__()"""

if __name__ == '__main__':
	obj1 = SequenceIteratorT1([2,4,3,6,2])
	obj2 = iter(obj1)
	for i in xrange(0,5):
		print obj1.next()
	print "Trying the second Class"
	obj11 = SequenceIteratorT2([2,4,3,6,2])
	obj22 = iter(obj11)
	for i in xrange(0,5):
		print obj22.next()

	print "Trying out reversed"	
	k= reversed(obj11)
	#k1= reversed(obj1) this will not work we have to implement the __reversed__() function for this to work
	for i in k:
		print i

		