from __future__ import division
l=[1,2,3,4,5,6,7,8,9]
for i in l:
	try:
		print i//0
	except ZeroDivisionError as e:
		print e
# file tryout
print "----------------------------------------------"
try:
	fp=open("D:\\Python_DS\\garbage.txt",'r')
	for word in fp:
		print word
except IOError as er:
	print e