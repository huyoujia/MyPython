list = []
def cal_(month,dic,count):#用来计算，无论mode，都需要计算
	money = 0
	sum = 0
	for i in range(1,count+1):
		if dic <= 6:
			money = 3
		elif dic > 6 and dic <= 12:
			money = 4
		elif dic > 12 and dic <= 22:
			money = 5
		elif dic > 22 and dic <= 32:
			money = 6
		elif dic > 32:
			if (dic-32)%20 ==0:
				money = 6+(dis-32)/20
			else:
				money = 16+int((dic-32)/20)+1
		if sum >= 100 and sum < 150:
			money = money*0.8
		elif sum >= 150 and sum <400:
			money = money*0.5
		sum += money
	list.append({month:sum})
	global money_total,count_total
	money_total += sum
	count_total += count
	
def show_input():
	dic = float(input("请输入距离:"))
	month = int(input("请输入月份:"))
	count = int(input("请输入每天的次数"))
	if month <= 12 and month >= 1:
		count = count*30
		return month,dic,count
	elif month <= 0 or month > 12:
		print("输入有误")

def show_output():
	for i in list:
		for k,v in i.items():
			print("%s月花了%.2f元" % (k,v))
	print("总共花了%.2f元,坐了%d次" % (money_total,count_total))

def menu():
	while True:
		model = int(input("菜单  1:乘坐 2:计算\n"))
		if model == 1:
			month,dic,count = show_input()
			if month != None :
				cal_(month,dic,count)
		elif model == 2: 
			show_output()

money_total = 0
count_total = 0

menu()
