information = "欢迎进入个人信息系统"
print(information.center(20,"*"))
list = []
while True:
	model = int(input("请选择功能 1:新增 2:查看 3:修改 4:删除 5:退出"))
	if model == 1:
		name = input("请输入名字")
		age = int(input("请输入年龄"))
		sex = input("请输入性别")
		work = input("请输入工作")
		list.insert(0,name)
		list.insert(1,age)
		list.insert(2,sex)
		list.insert(3,work)
		print(list)
	elif model == 2:
		position = int(input("请输入索引"))
		if position >= 0:
			if position >= len(list):
				print("输入错误")
		else:
		print(list[position])
	elif model == 3:
		oldname = input("请输入名字")
		newname = input("请输入新的名字")
		list[0] = newname
		print(list)
	elif model == 4:
		delname = input("请输入你要删除的名字")
		list.remove(delname)
		print(list)
	elif model == 5:
		break
