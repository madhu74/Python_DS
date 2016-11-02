def kutt(n):
	k = 0
	for j,i in enumerate(n):
		if not isinstance(i,(int,float)):
			raise TypeError(i,"Must be a integer or a float type which is at index",j)
		else:
			k = k+i
	return k

l=[1,2,3,4,5]
nl=[1,2,3,4,"try"]
print kutt(l)
print kutt(nl)
