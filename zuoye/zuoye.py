'''
#第一题
for i in range(1,5001):
	if (i%5==0 and i%7==0):
		print(i)
'''
'''
#第二题
import random
computer = random.randint(1,100)
for i in range(1,11):
	me = int(input("请输入一个数字"))
	if me > computer:
		print("你输入的数字大了哟")
	elif me < computer:
		print("小了，这么简单还猜不到，笨蛋")
	else:
		print("哇偶，聪明，猜对了")
		break
'''
'''
#第四题
i = 1
while i <=9:
	if i<=5:
		print("*"*i)
	elif i>5:
		print("*"*(10-i))
	i+=1
'''

#第五题
for i in range(2,101):
	if(i==2 or i==3 or i==5 or i==7) or (i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0):
		print(i)

