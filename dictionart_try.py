# This is to explore dictionary. 
d={}
countr=0
fp = open("D:\\Python_DS\\garbage.txt",'r')
for i in fp.read():
	if i in d.values():
		continue
	else:
		d[countr] = i
		countr = countr+1
print "done"
for i in d.values():
	print "-----",i
print "=============="
k = list(d.values())
print k
print type(d.values()),"hmmm"
print "-------------------------"
print range(10)
print "-------------------------"
print xrange(10)
print "-------------------------"
print d.items()
print "***********************"
print d.viewitems()

# bottom line keys(),values() and items() creates lists
#instead use viewkeys(),viewvalues(),viewitems()
#for itreator use iterkeys(),itervalues(),iteritems()
