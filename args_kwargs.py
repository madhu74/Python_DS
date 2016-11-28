def icaniterateAnyThing(*args):
	for arg in args:
		print arg

def soParameterize(**kwargs):
	for item in kwargs.viewitems():
		print item

icaniterateAnyThing(1,2,3,4,5,6,7,8,"mama")

soParameterize(x=1,y=4,sting1="madhu")

# python doesnot support overloading but using *args and **kwargs we can create branches inside defanitions./