def funcs(x,y,z):
	return x,y,z

def funcs(x):
	return x

def funcs(x,y):
	return x,y

print funcs(1,2,3)
print funcs(1,2)
print funcs(1)
# Hence proved no function overloading possible