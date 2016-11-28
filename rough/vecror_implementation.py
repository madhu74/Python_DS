from random import randrange
class Vector(object):
	
	def __init__(self,value):
		self._coordinate = [0 for i in xrange(0,value)]
	
	def __len__(self):
		return len(self._coordinate)
	
	def __getitem__(self,index):
		return self._coordinate[index]
	
	def __setitem__(self,index,value):
		self._coordinate[index] = value

	def __add__(self,other):
		if len(self._coordinate) != len(other._coordinate):
			raise ValueError("The Dimensions of the two vectors should be same")
		result = Vector(len(self))
		for i in xrange(0,len(self)):
			result._coordinate[i] = self._coordinate[i] + other._coordinate[i]
		return result

	def __eq__(self,other):
		return self._coordinate == other._coordinate

	def __ne__(self,other):
		return not (self == other)

	def __str__(self):
		return "<"+str(self._coordinate[:])+">"

if __name__ == '__main__':
	k = Vector(5)
	j = Vector(5)
	for i in range(0,len(k)):
		k[i] = randrange(100,150)
		j[i] = randrange(150,200)
	print k
	print j
	sol = k+j
	print sol