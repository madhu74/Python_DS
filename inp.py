i=0
while i<10:
	
	try:
		r = input("Enter the text \n")
		if r =="stop":
			break
		print r.upper()
		i+=1
	except EOFError as e:
		print "oopsy",e
		raise