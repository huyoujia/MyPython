def adduser():#添加
	name = input("请输入名字\n")
	age = (input("请输入年龄\n"))
	sex = input("请输入性别\n")
	place = input("请输入籍贯\n")
	edu = input("请输入学历\n")
	mail = input("请输入邮箱\n")
	isrepeat = False
	for dic in list:
		if dic["name"] == name:
			isrepeat = True
			print("用户已存在，请重新输入")
			break
	if not isrepeat:
		list.append({"name":name,"age":age,"sex":sex,"place":place,"edu":edu,"mail":mail})
		print("操作成功")


#删除
def deluser():
	con = True
	while con:
		delname = input("请选择需要删除的用户\n")
		for dic in list:
			if dic["name"]== delname:
				list.remove(dic)
				break
		print("删除成功")
		goon = int(input("继续删除请按1,结束请按0"))
		if goon == 0:
			con = False
#修改
def changuser():
	con = True
	while con:
		change_Name = input("请输入要修改的用户\n")	
		option = int(input("请输入要修改的信息1名字 2年龄 3性别 4籍贯 5学历 6邮箱"))
		change = input("修改为:\n")
		list_Option = [0,"name","age","sex","place","edu","mail"]
		is_show = True
		for dic in list:
			for k,v in dic.items():
				if v == change_Name:
					is_show = False
					dic[list_Option[option]] = change
					print("修改成功")
		if is_show:
			print("查无此人")
		print(list)
		goon = int(input("继续修改请按1，结束请按0"))
		if goon == 0:
			con = False



def finduser():#查找
	con = True
	while con:
		findname = input("请输入你要查找的信息")
		for dic in list:
			if dic["name"] == findname:
				print(dic)
		goon = int(input("继续查找请按1 结束请按0"))
		if goon == 0:
			con = Flase


title = "名片管理系统"
print(title.center(50,"*"))
list=[]
def menu():
	while True:
		fn = int(input("请输入功能 1 添加 2 删除 3 修改 4 查找 5 退出"))
		if fn == 1:
			adduser()
		elif fn == 2:
			deluser()
		elif fn == 3:
			changuser()
		elif fn == 4:
			finduser()
		elif fn == 5:
			break
		else:
			print("")
	print(list)
#系统保存的账号和密码
account = "huyoujia"
pwd = 123456
def login():
	myAccount = input("请输入账号")
	myPwd = int(input("请输入密码"))
	if (myAccount == account) and (myPwd == pwd):
		print("登录成功") 
		menu()
	else:
		print("账号或密码错误")
login()
