'''
d = float(input("请输入到家的距离: (km)"))
#money表示每次乘坐地铁的费用 
sum = 0
for i in range(1,61):
	if d <= 6:
		money = 3
	elif d > 6 and d <= 12:
		money = 4
	elif d > 12 and d <= 22:
		money = 5
	elif d > 22 and d <= 32:
		money = 6
	elif d > 32:
		money = 6+(d-12)//20
	elif sum >= 100 and sum < 150:
		money = money*0.8
	elif sum >= 150 and sum < 400:
		money = money*0.5
	sum += money
print("你一共要支付%.2f元"%sum)
'''

d = float(input("请输入到家的距离: (km)"))
sum = 0
for i in range(1.61):
	if d <=10:
		money = 2
	elif d > 10:
		money = 2+(d-5)//5

