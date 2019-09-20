def divisior(a,b):
	c=min(a,b)
	for i in range(c,0,-1):
		if a%i==0 and b%i==0:
			return i
def multiple(a,b):
	return a*b//divisior(a,b)
if __name__ == '__main__':
	x=int(input('please input a positive integra:'))
	y=int(input('please input a positive integra:'))
	print(divisior(x,y),multiple(x,y))


