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