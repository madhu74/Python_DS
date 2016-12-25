#!/bin/python
#import sys
"""

arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

class fw(object):
    def __init__(self,temp):
        if len(temp) == 3:
            for i in xrange(3):
                
        
    def __str__(self):
        for i in self._temp:
            sys.stdout.write("\n")
            for j in i:
                if len(i)==1:
                    sys.stdout.write("  ")    
                    sys.stdout.write(str(j))
                    sys.stdout.write(" ")
                else:
                    sys.stdout.write(str(j))
                    sys.stdout.write(" ")
    def tot(self):
        total = 0
        for i in self._temp:
            total = total + sum(i)
        return total
        """
#!/bin/python
import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
temp = [[0,0,0],[0],[0,0,0]]

def tot(to):
    total = 0
    for i in to:
        total = total + sum(i)
    return total
large = -10000000000000
for i in xrange(len(arr)):
    for j in xrange(len(arr[i])):
        if i+2 < len(arr) and j+3 < len(arr[i])+1:
            temp[0] = arr[i][j:j+3]
            temp[1] = [arr[i+1][j+1]]
            temp[2] = arr[i+2][j:j+3] 
            if tot(temp) > large:
                large = tot(temp)
print large