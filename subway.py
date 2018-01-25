list = [] #用来记录每个月的地铁费用
allcount = 0 #用来记录一共坐了多少次地铁
#计算每个月的费用
def subway(dis,month,count):
	info = {}
	money = 0
	sum = 0
	global allcount
	allcount += count*30
	for i in range(0,count*30):
		if dis <= 6:
			money = 3
		elif dis > 6 and dis <= 12:
			money = 4
		elif dis > 12 and dis <= 22:
			money = 5
		elif dis > 22 and dis <= 32:
			money = 6
		elif dis > 32:
			if (dis - 32)%20 == 0:
				money = 6 +(dis - 32)/20
			else:
				money = 6 +(dis - 32)/20 + 1
		if sum >= 100 and sum < 150:
			money = money*0.8
		elif sum >= 150 and sum < 400:
			money = money*0.5


		sum += money
#用一个字典装月份和这月份的钱
	info[month] = sum
	list.append(info)

def money():
	sum = 0
	for i in list:
		for k,v in i.items():
			print("%d月花了%0.2f元"%(k,v))	
			sum += v
	return sum





def menu():
	loop = True
	while loop:
		model = int(input("菜单  1:乘坐  2:计算\n"))
		if model == 1:
			dis = float(input("请输入距离"))
			month = int(input("请输入月份"))
			count = int(input("请输入每天的次数"))
			if month >= 13 or month < 0:
				print("输入的不合法")
			elif count <= 0:
				print("输入的不合法")
			else:
				subway(dis,month,count)
		
		else:
			result = money()
			print("总共花了%0.2f元,一共坐了%d次地铁"%(result,allcount))
			loop = False

menu()
