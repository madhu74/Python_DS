""" also consider 
class Base(object):
    def go(self):
        raise NotImplementedError("Please Implement this method")


class Specialized(Base):
    def go(self):
        print "Consider me implemented"

"""
from abc import ABCMeta,abstractmethod

class Sequence(object):
	__metaclass__ = ABCMeta
	 
	@abstractmethod
	def __len__(self):      #We have to give return for abstract method in python 2.7 https://pymotw.com/2/abc/
		return        

if __name__ == '__main__':
	
	c = Sequence()
	"""print dir(Sequence())
	for i in dir(Sequence()):
		print i,getattr(Sequence(),i)"""