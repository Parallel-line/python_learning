from math import *
a=int(input('please input a positive integra:'))
b=int(input('please input a positive integra:'))
c=min(a,b)
factor=1
for i in range(c,0,-1):
	print(i,a%i,b%i)
	if(a%i==0 and b%i==0):
		factor=i
		print('%d and %d 最大公约数为%d'%(a,b,factor))
		print('%d and %d 最小公倍数为%d'%(a,b,a*b//factor))
		break
