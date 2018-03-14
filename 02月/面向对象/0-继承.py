class Animal(object):
	
	def __init__(self):
		self.variety ="动物"
	#方法 
	def print_name(self):
		print("liuboyu")

class Dog(Animal):
	def run(self):
		print("the dog is running")

	def cry(self):
		print('the dog is crying')

	def print_name(self):
		#super().print_name() #super()保存父类的方法 super是一个函数 后加()
		print("ffrtgr")


#class Cat(Animal):
#	def mew(self):
#		print("the cat is mew")
#	def cry(self):
#		print('the cat is crying')
#
#class Zajiao(Cat,Dog):
#	pass
dd = Dog()
dd.print_name() #重写父类的方法

#a = Zajiao()
#a.variety = "猫狗兽"
#a.print_name()
#a.run()
#a.mew()
#a.cry()
#huahua = Dog()
#huahua.variety = "中华田园犬"
#huahua.print_name()
#huahua.run()



#hh = Animal()
#hh.variety = "哈巴狗"
#hh.print_name()

