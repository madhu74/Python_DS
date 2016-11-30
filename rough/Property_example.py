"""dir(property())

['__class__', '__delattr__', '__delete__', '__doc__',  '__format__', '__get__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__set__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'deleter', 'fdel', 'fget', 'fset', 'getter', 'setter'] 
Ref: https://www.programiz.com/python-programming/property
"""
class MySampleClass(object):

	def __init__(self,default=0):
		self._default = default

	@property					#property(fget=None, fset=None, fdel=None, doc=None) getter,setter and deleter
	def value(self):
		return self._default

	@value.setter
	def value(self,temp_default):
		self._default = temp_default

	@value.deleter
	def value(self):
		del(self._default)

	def normal(self):                  # Attributes but not changable?
		return "hello"

if __name__ =='__main__':
	c = MySampleClass(10)
	print c.value
	c.value = 200
	print c.value
	del(c.value)
	#print c.value
	print c.normal