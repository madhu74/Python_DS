from __future__ import division
l=[1,2,3,4,5,6,7,8,9]
for i in l:
	try:
		print i//0
	except ZeroDivisionError as e:
		print e