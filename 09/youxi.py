def taken():
	list = ["M4a1","M16","Ak47",'p1911','98K']
	import random
	import time
	get_time = random.randint(1,3)
	time.sleep(get_time)
	gun = random.sample(list,1)
	print(gun)		
while True:	
	taken()






def login(myaccout,mypwd):
	if (myaccout == account) and (mypwd == pwd):
		print("登录成功 ，开始游戏")
		taken()
	else:
		print("登录失败") 
'''
accout = "huyoujia"
pwd = "123456"
myaccount = input("请输入一个账号")
mypwd = int(input("请输入一个密码"))

login(myaccount,mypwd)

'''
