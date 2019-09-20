def main():
	str1 = 'hello world'
	print(len(str1))    #输出字符串的长度
	print(str1.capitalize())  #将字符串首字母大写
	print(str1.upper())   #将字符串的每个字母都大写
	print(str1.find('or')) #查找子串在字符串在的位置,输出的是r所在位置，字符串第一个位置是0
	print(str1.find('shit')) #如果找不到就返回-1
	print(str1.startswith('He')) #判断开头是不是这个，如果不是，返回False
	print(str1.startswith('hel')) #如果是，返回True
	print(str1.endswith('!'))  #判断结尾是不是，如果不是，返回False
	print(str1.center(30,'*')) #将字符串以指定的宽度居中并在两侧填充指定的字符
	print(str1.rjust(20,' ')) #将字符串以制定的宽度靠右放置左侧填充指定的字符
	str2 = 'abc123456'
	print(str2[2])  #输出位置第2的字符，开头第一个位置是0
	print(str2[2:5])  #字符串切片，输出的是c12，第2，3，4位
	print(str2[2:])  #从第2位输出
	print(str2[2::2]) #输出从2位开始，第2，4，6，8位
	print(str2[::2]) #输出的是0，2，4，6，8位
	print(str2[::-1])  #倒着输出序列
	print(str2[-3:-1]) #最后一位是-1，输出-3，-2
	print(str2.isdigit()) #检查字符串是否以数字组成
	print(str2.isalpha()) #检查字符串是否以字母组成
	print(str2.isalnum()) #检查字符串是否以字母和数字组成
	str3 = ' jackfrued@126.com '
	print(str3)
	print(str3.strip()) #获得字符串修剪左右两侧空格的拷贝
if __name__=='__main__':
	main()