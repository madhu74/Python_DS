'''this the main operation in insertion-sort is like a typical insert operation in a list or an array, 
we have to make place for the new value insde the array or the list (ref: j=j-1(insert),j=j+1(remove) )'''

def insertion_sort(data):
	for i in xrange(len(data)):
		j = i
		curr = data[i]
		while j > 0 and data[j-1] > curr:
			data[j] = data[j-1]
			j = j-1
		data[j] = curr

if __name__ =='__main__':

	l = [3,3,63,73,68,12,98]
	insertion_sort(l)
	print l