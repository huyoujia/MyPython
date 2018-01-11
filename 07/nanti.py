list = []
def print_user():
	while True:
		dic = {}
		model = int(input("请选择1编辑 2退出"))
		if model == 1:
			name = input("请输入名字")
			age = int(input("请输入年龄"))
			if not list:
				dic["name"]= name
				dic["age"] = age
				list.append(dic)
			else:
				isrepeat = False #假设不重复
				for i in list:
					for k,v in i.items():
						if v == name:
							isrepeat = True
							print("你输入重复了,请重新输入")
							break
				if not isrepeat:
					dic["name"]=name
					dic["age"]=age
					list.append(dic)
			print(list)
		if model == 2:
			break
		
print_user()
