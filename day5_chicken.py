from math import *
for x in range(0,20):
	for y in range(0,34):
		# if (100-x-y)%3==0 and (8*x+14*y==200):
		if (100-x-y)%3==0 and (3*x+5*y+(100-x-y)/3==100):
			print(x,y,100-x-y)

