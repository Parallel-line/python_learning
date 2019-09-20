from math import *
a=1
b=1
print(a,b,end=' ')
for i in range(20):
	c=a+b
	a=b
	b=c
	print('%d'%c,end=' ')
print()
