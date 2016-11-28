""" This is a simple example of a typical inheritance implementation please check how the super() is implemented
    for python 3 we sue super().__init_()
    but for python 2 we use super(current_class_name,current_class_object_reference).__init__() also check banking function
"""
class Progression(object):

	def __init__(self,start=0):
		self._current = start

	def _advance(self):
		self._current += 1

	def next(self):
		if self._current is None:
			raise StopIteration()
		else:
		    answer = self._current
		    self._advance()
		    return answer

	def __iter__(self):
		return self

	def print_progression(self,n):
		print " ".join(str(next(self)) for i in xrange(n))

class ArithmeticProgression(Progression):

	def __init__(self,increment=1,start = 0):
		super(ArithmeticProgression,self).__init__(start)
		self._increment = increment

	def _advance(self):
		self._current += self._increment

class GeometricProgression(Progression):

	def __init__(self,base=2,start =1):
		super(GeometricProgression,self).__init__(start)
		self._base = base

	def _advance(self):
		self._current *= self._base

if __name__ =='__main__':
	p = Progression()
	p.print_progression(10)
	# Arithmetic progression 
	print '-------Arithmetic progression------'
	q = ArithmeticProgression(2,9)
	q.print_progression(10)
	print '-------Geometric progression------'
	r = GeometricProgression(3,2)
	r.print_progression(10)
