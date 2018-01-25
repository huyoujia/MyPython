class Food(object):
	def __init__(self):
		#地瓜的生熟程度
		self.grow = 0
		#返回给用户的字符串
		self.str = ""
		#地瓜的配料列表
		self.condiments = []
	def cook(self,time):
		self.grow += time
		if self.grow > 8:
			self.str = "烤成炭了"
		elif self.grow > 5:
			self.str = "烤好了"
		elif self.grow >3:
			self.str = "半生不熟"
		else:
			self.str = "生的"
	def __str__(self):
		info = ""
		if len(self.condiments) > 0:
			for temp in self.condiments:
				info = info + temp
			info = self.str	+'('+ info+')'		
		return info
	def addCondiments(self,condiments):
		self.condiments.append(condiments)
		


	
sweetphoto = Food()
#print(sweetphoto.grow)
#print(sweetphoto.str)
#print(sweetphoto.cooked)
#sweetphoto.cook(5)
#print(sweetphoto.grow)
#print(sweetphoto.str)
print("-----有了一个地瓜，还没有烤地瓜-----")
print("sweetphoto.grow")
print("sweetphoto.str")
print("sweetphoto.cooked")
print("接下来进行烤地瓜了")
print("地瓜已经烤了四分钟了")
sweetphoto.cook(4)
print(sweetphoto)
print("地瓜又烤了三分钟")
sweetphoto.cook(3)
print(sweetphoto)
print("----接下来添加番茄酱----")
sweetphoto.addCondiments("番茄酱")
print(sweetphoto)
print("地瓜又经过五分钟烤")
sweetphoto.cook(5)
print(sweetphoto)
print("-----接下来添加芥末了----")
sweetphoto.addCondiments("芥末")
print(sweetphoto)
