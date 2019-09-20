def element():
	list1 = [1,3,5,7,100]
	print(list1)
	list2 = ['hello'] * 5 #表示有五个hello
	print(list2)
	print(len(list1))
	print(list1[0])
	print(list1[4])
	print(list1[-1])  #倒数第一个元素，即第四个元素
	print(list1[-3])
	list1[2]=300  #替换第二个元素列表和字符串的头一个元素都是第0元素
	print(list1)
	list1.append(200) #在列表的最后加上200这个元素
	list1.insert(3,400) #在第1个元素的前面插入400这个元素
	list1+=[1000,2000] #在列表的末尾加上这一串子串
	print(list1)
	print(len(list1))
	list1.remove(3) #删除‘3’这个元素
	if 2 in list1:
		list1.remove(2)
	del list1[0]  #删除列表的头元素
	print(list1)
	list1.clear() #清空列表
	print(list1)
def slice(): #与数字列表操作一致
	fruits=['grape','apple','strawberry','waxberrt']
	fruits+=['pitaya','pear','mango']
	for fruit in fruits:
		print(fruit.title(),end=' ') #输出首字母大写的字符
		#print(fruit,end=' ')
	print()
	fruits2=fruits[1:4]
	print(fruits2)
	#fruits3=fruits 没有复制过去
	fruits3=fruits[:]  #将列表复制给新的列表
	print(fruits[-3:-1])
	print(fruits3)
	print(fruits[::-1])
def sort():
	list1=['orange','apple','zoo','internationalization','blueberry']
	list2=sorted(list1)   #默认按照首字母排序
	list3=sorted(list1,reverse=True) #添加了reverse=true，则按照首字母反过来排序
	list4=sorted(list1,key=len) #按照字符长度排序
	print(list1)
	print(list2)
	print(list3)
	print(list4)
	list1.sort(reverse=True) #之间在字符上排序，按照首字母倒过来的顺序安排
	print(list1)
import sys
def generate():
	f=[x for x in range(1,10)]
	print(f)
	f=[x+y for x in 'ABCDE' for y in '1234567'] #创建的元素已经准备就绪
	print(f)
	#f=[x**2 for x in range(1,1000)]  #不同的生成方法
	f=(x**2 for x in range(1,1000)) #创建一个生成器对象，需要数据的时候再运算得到
	print(sys.getsizeof(f))  #查看对象占用内存的字节数
	print(f)
	for val in f:
		print(val)
def main():
	#element()
	#slice()
	#sort()
	generate()
if __name__ == '__main__':
	main()