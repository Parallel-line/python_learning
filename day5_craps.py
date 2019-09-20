from math import *
from random import *
money=1000
result=True
debt=int(input('请下注:'))
a=randint(1,6)  #产生一到六之间的整数型随机数
b=randint(1,6)
if a+b==7 or a+b==11:
	result=False
	money+=debt
	print('the player wins')
elif a+b==2 or a+b==3 or a+b==12:
	result=False
	money-=debt
	print('zhuangjia wins')
c=a+b
while result and money>0:
	debt=int(input('请下注：'))
	a=randint(1,6)  #产生一到六之间的整数型随机数
	b=randint(1,6)
	if a+b==c:
		result=False
		money+=debt
		print('the player wins')
	elif a+b==7:
		result=False
		money-=debt
		print('zhuangjia wins')


