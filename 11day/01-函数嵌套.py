'''#函数嵌套调用 
def sum(x,y):
	def sum1(z):
		return x+y+z

	return sum1

result = sum(2,4)
d = result(23)
print(d)
'''
'''
#用while阶乘
def Num(count):
	result = 1
	while count >= 1:
		result *= count
		count -= 1
	return result


print(Num(5))

#5!= 5*4*3*2*1
'''
#递归函数
def calNum1(num):
	if num > 1:
		return num*calNum1(num-1)
	else:
		return num
print(calNum1(5))
