def is_palindrome(num):
	result=0
	temp=num
	while temp>0:
		result=result*10+temp%10  #从最后一位开始，尾巴每增加一位，前面就乘以10
		temp//=10
	return result==num
if __name__=='__main__':
	test=int(input('plese input：'))
	print(is_palindrome(test))