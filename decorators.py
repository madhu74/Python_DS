def double(myfunc):
	def double_inside():
		return myfunc()*2
	return double_inside

def alternate_double(myfunc):
	return myfunc()*2

def oddnumber():
	return 3

#This is returning a function
evennumber = double(oddnumber)
print evennumber()

# This is not returning any function but just value. 
alternate_even = alternate_double(oddnumber)
print  alternate_even

#to alter the existing function value we use
oddnumber = double(oddnumber)
print oddnumber()

#the above alteration can be done by using decorators
