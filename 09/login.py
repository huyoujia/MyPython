def register(account,pwd):
	if is_phone(account):
		print("注册成功")
		login(account,pwd)

def login(account,pwd):
	if is_phone(account):
		print("登录成功")

def is_phone(account):
	if len(account) == 11:
		return 1
	else:
		print("手机号不合法，请重新输入")
		return 0

account = input("请输入一个账号")
pwd = int(input("请输入一个密码"))


register(account,pwd)
	
