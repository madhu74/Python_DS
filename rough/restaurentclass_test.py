class Restaurent(object):
    def __init__(self,bankrupt):
        self.bankrupt = bankrupt
    def open_branch(self):
    	if not self.bankrupt:
    		print "Welcome to the new branch"

x=Restaurent(False)
print x.bankrupt
#print Restaurent.bankrupt
#Restaurent.bankrupt = True
print x.bankrupt
x.open_branch()
#self in a function is not a keyword, it is but a placeholder that holds the instance of the class that that function belongs to.
#we can also use other varuavles in the place of self,but prefered not to. If a values is defined outside the __init__() finction it is called class variable.
# __init__() and __call__(): the first builds an instance of Class up, the second makes such instance callable as a function would be without impacting the lifecycle of the object itself (i.e. __call__ does not impact the construction/destruction lifecycle) but it can modify its internal state (as shown below).