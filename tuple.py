def tuple():
	t=('linyu','20','female','河南')
	print(t)
	print(t[0])
	print(t[3])
	for member in t:
		print(member)
	#t[0]='lin'  #tuple不支持这种操作，不能直接修改元组中的单个元素
	t=('lin','18','male','江苏')
	print(t)
	person=list(t)
	print(person)
	person[0]='yu'
	print(person)
	fruit_list=['apple','banana','orange']
	fruit_tuple=tuple(fruit_list)
	#print(fruit_tuple)

def main():
	tuple()

if __name__ == '__main__':
	main()