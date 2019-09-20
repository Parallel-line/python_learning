year=int(input('please input the year: '))
# if (year%400==0):
# 	print('True')
# else:
# 	print('False')
is_leap=(year%4==0 and year%100!=0 or year%400==0)
print(is_leap)