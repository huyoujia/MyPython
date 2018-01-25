list = []
def add():#进入主页面，我想要的宝贝
	dic = {}
	name = input("请输入你要增加的宝贝")
	place = input("请输入要增加宝贝的产地")
	attribute = input("请输入要增加宝贝的属性")
	list.append({"name":name,"place":place,"attribute":attribute})
	print(list)
	print("添加购物车成功")	

def deluser():#删除
	con = True
	while con:
		delname = input("请选择需要删除的选择")
		for dic in list:
			if dic["name"] == delname:
				list.remove(dic)
				break
		print("删除成功")
		goon = int(input("继续请按1，结束请按0"))
		if goon == 0:
			con = False


def change():#修改
	con = True
	while con:
		change_name = input("请输入要修改的宝贝")
		option = int(input("请输入要修改的修改的信息(1)名字 (2)产地(3)属性"))
		change = input("修改为:")
		list_Option = [0,"name","place","attribute"]
		for dic in list:
			for k,v in dic.items():
				if v == change_name:
					dic[list_Option[option]]=change			
		print("修改成功")
		print(list)
		goon = int(input("继续修改请按1,结束请按0"))
		if goon == 0:
			con = False

def find(): #查看
	con = True
	while con:
		find_Name = input("请输入你查询的选项")
		for dic in list:
			if dic["name"] == find_Name:
				print(dic)
		goon = int(input("继续查询请按1，结束请按0"))
		if goon ==0:
			con = False 

def payment():#付款
	balance = 200
	payment = int(input("请输入你花了多少钱"))
	if payment <= balance:
		yuer = balance - payment
		print("剩余%d元"%yuer)
	elif payment > balance:
		print("sorry，超支了")
	 
				
def menu():#菜单
	while True:
		fn = int(input("请选择功能 1添加 2删除 3修改 4 查找 5 付款 6退出"))
		if fn == 1:
			add()
		elif fn == 2:
			deluser()
		elif fn == 3:
			change()
		elif fn == 4:
			find()
		elif fn == 5:
			payment()
		elif fn == 6:
			break
		else:
			print("sorry，没有这个功能")


def login():
	account = "huyoujia"#系统定义的
	pwd = 123456
	myAccount = input("请输入一个账号")
	myPwd = int(input("请输入密码"))
	if (myAccount == account) and (myPwd == pwd):
		print("登录成功")
		menu()
	else:
		print("登录失败，请重新登录")


#淘宝登录系统
title = "淘宝购物系统"
print(title.center(50,"*"))


login()
