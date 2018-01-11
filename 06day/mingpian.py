def adduser():
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



def deluser():
	con = True
	while con:
		delname = input("请选择需要删除的用户\n")
		for dic in list:
			if dic["name"]== delname:
				list.remove(dic)
				break
		print("你已成功删除%s"%deluser)
		goon = int(input("继续删除请按1,结束请按0"))
		if goon == 0:
			con = False

def changuser():
	change = input("请输入需要修改的用户\n")
	for z in list:
		if z["name"] == change:
			while True:
				you = input("请输入需要修改的项 1姓名 2年龄 3性别 4籍贯 5学历 6邮箱 ")
				if you == "1":
					names = input("请输入你要改的名字")
					z["name"] = names
					print("已经成功修改为%s"%names) 		
				elif you == "2":
					ages = input("请输入你要改的年龄")
					z["age"] = ages
					print("成功修改年龄为:%s"%ages)
				elif you == "3":
					sexs = input("请输入你要修改的性别")
					z["sex"] = sexs
					print("成功修改性别为:%s"%sexs)
				elif you == "4":
					places = input("请输入新的地方")
					z["place"] = places
					print("修改籍贯为:%s"%places)
				elif you == "5":
					edus = input("你要改成什么学历")
					z["edu"] = edus
					print("修改学历为:%s"%edus)
				elif you == "6":
					mails = input("你要改为什么邮箱")
					z["mail"] = mails
					print("修改邮箱为:%s"%mails)


def finduser():#查找
	con = True
	while con:
		findname = input("请输入你要修改的信息")
		for dic in list:
			if dic["name"] == findname:
				print(dic)
		goon = int(input("继续查找请按1 结束请按0"))
		if goon == 0:
			con = Flase


title = "名片管理系统"
print(title.center(50,"*"))
list=[]
while True:
	fn = int(input("请输入功能 1 添加 2 删除 3 修改 4 查找 5 退出"))
	if fn == 1:
		adduser()
	elif fn == 2:
		deluser()
	elif fn == 3:
		changeuser()
	elif fn == 4:
		finduser()
	elif fn == 5:
		break
	else:
		print("")
print(list)
print(70,"*")
	
