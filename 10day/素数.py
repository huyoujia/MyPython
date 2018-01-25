'''#不推荐使用这种方式
def prime_number():
	list=[]
	for i in range(2,101):
		if (i==2 or i==3 or i==5 or i==7) or (i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0):
			list.append(i)
	return list
result=prime_number()
print(result)
'''

def prime_number():
	list=[]
	for i in range(2,101):
		is_num = True
		for j in range(2,i):
			if i%j==0:
				is_num = False
				break
		if is_num:
			print(i)
			list.append(i)
	return list
result=prime_number()
print(result)
