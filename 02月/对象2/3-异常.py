class Test(object):
	def __init__(self, switch):
		self.switch = switch
		
	def cala(self, a, b):
		try:
			return a/b
		except Exception as result:
			if self.switch:
				print("捕获开启，已经捕获到了异常，信息如下：")
				print(result)
			else:
				#重新抛出这个异常，此时就不会被这个异常处理捕获到，从而触发默认的异常处理

				raise 

a = Test(True)
a.cala(11,0)
print("-"*34)
a.switch = False
a.cala(11,0)










'''
def sr():
	pwd = input("请输入密码")
	#判断长度
	if len(pwd) >= 8:
		print("密码正确")
	else:
		print("密码错误")
	#密码长度不够，需要抛出异常
	#需要创建异常对象 - 使用异常的错误信息字符串作为参数
		ec = Exception("密码长度不够") #python中提供了一个Exception 异常类  使用raise关键字抛出异常对象
		raise ec


try:
	user_pwd = sr()

except Exception as result:
	print("发现错误：%s"%result)

else:
	print("输入正确")

finally:
	print("输出了一串数字")
'''
'''
def demo1():
	num = int(input("请输入一个整数"))
	return num

def demo2():
	return demo1()

try:
	print(demo2())

except ValueError:
	print("请输入正确的整数")

except Exception as result:
	print("未知错误:%s"%result)

'''
'''
try:
	num = int(input("请输入整数"))
	result = 8/num
	print(result)

except ValueError:
	print("请输入正确的整数") 


except ZeroDivisionError:
	print("除0错误")

except Exception as result:
	print("未知错误%s"%result)

else:
	print("正常执行")

finally:
	print("执行完成")
'''
