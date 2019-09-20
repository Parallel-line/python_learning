row=int(input('请输入行数：'))
for i in range(row):     #range(start,stop,step)左闭右开区间
	for _ in range(i+1):  #_表示之后不会再用到的变量
		print('*',end='') #end表示不换行
	print()  #换行


for i in range(row):
	for j in range(row-i-1):
		print(' ',end='')
	for j in range(row-i-1,row):
		print('*',end='')
	print()


for i in range(row):
	for j in range(2*row-1):
		if(j<row-i-1):
			print(' ',end='')
		elif(j<row+i):
			print('*',end='')
		# else:
		# 	print(' ',end='')
	print()

