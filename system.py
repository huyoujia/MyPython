list = []
dic = {}
def addUser():#添加
	con = True
	while con:
		name = input("请输入名字\n")
		age = int(input("请输入年龄\n"))
		sex = input("请输入性别\n")
		isrepeat = True
		for dic in list:
			if dic["name"] == name:
				isrepeat = False
				print("用户已经存在")
				break
		if isrepeat:
			list.append({"name":name,"age":age,"sex":sex})
		print("操作成功")
		mode = int(input("继续请按1，结束请按0"))
		if mode == 0:
			con = False
			break
	
def delUser():#删除
	con = True
	while con:
		del_info = input("请输入你要删的信息\n")
		is_show = True
		for dic in list:
			if dic["name"] == del_info:
				is_show = False
				list.remove(dic)
				break
			print("删除成功")
		if is_show:
			print("sorry，你要删除的人我们本来就没有")
		mode = int(input("继续请按1，结束请按0"))
		if mode == 0:
			con = False
			break
			
def change():
	con = True
	while con:
		change_name = input("请输入要修改的用户\n")
		option = int(input("请输入要修改的信息1名字 2年龄 3性别"))
		changes = input("修改为:\n")
		list_option = [0,"name","age","sex"]
		is_show = True
		for dic in list:
			for k,v in dic.items():
				if v == change_name:
					is_show = False
					dic[list_option[option]] = changes
					print("修改成功")
					print(list)
		if is_show:
			print("查无此人")
		mode = int(input("继续修改请按1，结束请按0"))
		if mode == 0:
			con = False

def find(): #查找
	con = True
	while con:
		find_info = input("请输入你要查找的信息")
		is_show = True
		for dic in list:
			if dic["name"] == find_info:
				is_show = False
				print(dic)
		if is_show:
			print("没有你要找的人")
		mode = int(input("继续请按1，结束请按0"))
		if mode == 0:
			con = False
			break
			


tip = "学生管理系统"
print(tip.center(40,"*"))

def menu():
	while True:
		model = int(input("请选择模式1增 2删 3改 4查 5退出\n"))
		if model == 1:
			addUser()
		elif model == 2:
			delUser()
		elif model == 3:
			change()
		elif model == 4:
			find()
		elif model == 5:
			break
		else:
			print("你选择的模式不在我的范围内，请重新选择")
menu()
