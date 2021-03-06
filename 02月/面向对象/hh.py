'''
class base(object):
	def test(self):
		print('----base test----')
class A(base):
	def test(self):
		print('----A test----')

# 定义一个父类
class B(base):
	def test(self):
		print('----B test----')

# 定义一个子类，继承自A、B
class C(A,B):
	pass


obj_C = C()
obj_C.test()

'''
class Cat(object):

	def __init__(self, name, color="白色"):
		self.name = name
		self.color = color

	def run(self):
		print("%s--在跑"%self.name)


# 定义一个子类，继承Cat类如下:
class Bosi(Cat):

	def setNewName(self, newName):
		self.name = newName

	def eat(self):
		print("%s--在吃"%self.name)


bs = Bosi("印度猫")
print('bs的名字为:%s'%bs.name)
print('bs的颜色为:%s'%bs.color)
bs.eat()
bs.setNewName('波斯')
bs.run()

