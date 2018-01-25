'''
def num(a):
	if a > 1:
		return a*num(a-1)
	else:
		return a
result = num(10)
print(result)
'''

def num(a,b,opt):
	return a+b
a = int(input("请输入一个数字"))
b = int(input("请输入另一个数字"))
result = num(a,b,lambda a,b:a+b)
print(result)
