'''
try:
	print(a)
except NameError as result:
	print(result)

try:
	open('a.txt')
except Exception as result:
	print("捕捉到了异常")
	print("异常信息为：",result)
try:
	print(num)
except: 

	print("产生了错误")

import time
try:
	f = open("test.txt")
	try:
		while True:
			content = f.readline()
			if len(content) == 0:
				break
			time.sleep(2)
			print(content)
	except:
		pass
	finally:
		f.close()
		print("关闭文件")
except:
	print("没有这个文件")
'''
