from math import *
a=int(input('please input a positive integra: '))
b=int(sqrt(a))
result=True
for i in(2,b+1):
	if a%i==0:
		result=False
		break
if result and a!=1:
	print('%d is prime'%a)
else:
	print('%d is not prime'%a)
	
