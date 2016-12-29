from __future__ import division

def binary_search(data,target,start,stop):
	
	if start > stop : # stopping factor nothing found
		return (False,None)
	else:
		mid =(start+stop)//2
		if target == data[mid]:
			return(True,mid)
		elif target > data[mid]:
			return binary_search(data,target,mid+1,stop)
			#binary_search(data,target,mid+1,stop)
		else:
			return binary_search(data,target,start,mid-1)
			#binary_search(data,target,start,mid-1)

if __name__ =='__main__':
	print binary_search([1,2,4,5,6,37,67],12,0,len([1,2,4,5,6,37,67]))