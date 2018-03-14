'''
class Human(object):
	#定义对象的属性
	def __init__(self,eyes):
		self.eyes = eyes
	def __str__(self):
		return "你真可爱"
	#对象方法
	def walk(self,name):
		print(name + " you are walking")


huyoujia = Human("black")
huyoujia.walk('huyoujia')
print(huyoujia)

print(id(huyoujia))
'''

class Tool(object):
	count = 0
	@classmethod
	def too_show(cls):
		print("创建了%d"%Tool.count)
		print("创建了%d"%cls.count)

	def __init__(self,name):
		self.name = name
		Tool.count += 1	


tool1 = Tool("斧头")
tool2 = Tool("锤子")

Tool.too_show()
		
