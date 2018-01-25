#缺省参数
def sum(a,b=34):
	c=a+b
	return c
result=sum(1)
print(result)


#求1+100
def sum1(a,b):
	c=a+b
	return c
result1=sum(1,100)
print(result1)


#用while循环求0-100的和
def sum2(n):
	result2=0
	i=1
	while i <= n:
		result2=result2+i
		i+=1
	return result2
result3=sum2(100)
print(result3)

