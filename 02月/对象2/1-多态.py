class Dog(object):
	def __init__(self,name):
		self.name = name
	def game(self):
		print(self.name + "在玩耍")

class Xiaotiandog(Dog):
	def game(self):
		print(self.name +"在天上玩耍")

class Human(object):
	def __init__(self,name):
		self.name = name

	def game_with_dog(self,dog):
		print("%s和%s在玩耍"%(self.name,dog.name))


feitianwangcai = Xiaotiandog("飞天旺财")
feitianwangcai.game()

#多态：不同的对象调用相同的方法产生不同的结果
