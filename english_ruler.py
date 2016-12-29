# this is an exam for recursion, English ruler implementable.
# three important steps, an interval with central tick lenght L contains
#*an interval with central tick lenght L-1
#a tick of length L
#*an interval with central tick length l-1

def draw_line(tick_length,tick_lable=''):
	tick ="-"
	line =tick*tick_length
	if tick_lable:
		line = line+' '+tick_lable
	print line

def draw_interval(centerlength):
	if centerlength > 0 :
		draw_interval(centerlength-1)
		draw_line(centerlength)
		draw_interval(centerlength-1)

def draw_ruler(numb_inches,majorlength):
	draw_line(majorlength,str(0))
	for i in range(1,numb_inches+1):
		draw_interval(majorlength)
		draw_line(majorlength,str(i))

if __name__ == '__main__':
	draw_ruler(3,5)
