def fibo(n):
	if n<=1:
		return (n,0)
	else:
		a,b = fibo(n-1)
		print a,b,'-----',n
		return (a+b,a)

if __name__ == '__main__':
	print fibo(10)