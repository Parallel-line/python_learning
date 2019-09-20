from math import *
for i in range(1,10000):
	sum=0
	for j in range(1,i):
		if i%j==0:
			sum+=j
			# print(i,j,sum)
	if sum==i:
		print('%d is perfect number'%i)

