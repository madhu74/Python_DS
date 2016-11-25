from __future__ import division

class Range(object):

	def __init__(self,start,stop=None,step=1):
		if step == 0:
			raise ValueError('Step size cannot be 0')
		if stop == None:
			start,stop = 0,start
		self._length = ((stop - start +step - 1) //step)
		self._start = start
		self._stop = stop
		self._step = step

	def __len__(self):
		return self._length

	def __getitem__(self,k):
		if k<0:
			k+= len(self)

		if not 0 <= k < len(self):
			raise IndexError('index out of range')

		return self._start + k*self._step

if __name__ == '__main__':
	r = Range(0,10,2)
	print len(r)
	for i in r:
		print i