'''#不定长参数 求这几个数值的和
def sum_(a,b,c,*args,**kwargs):
	sum = 0
	print(a)
	print(b)
	print(c)
	print(args)
	print(kwargs)
	for i in args:
		sum +=i
	for k,v in kwargs.items():
		sum +=v
	sum=sum+a+b+c
	return sum
result = sum_(1,2,3,4,5,6,7,8,10,age=56,name=300)
print(result)
'''#不定长参数的另一种表达方式
def sum_(a,b,c,*args,**kwargs):
	print(a)
	print(b)
	print(c)
	print(args)
	print(kwargs)
A=(4,5,67,85,43,6)
B={"name":23,"age":3}
sum_(1,2,3,*A,**B)
