class people:
	name = ''
	age = 0
	__weight = 0
	def __init__(self,n,a,w):
		self.name = n
		self.age = a
		self.weight = w
	def speak(self):
		print("%s说，我今年%s岁了" % (self.name,self.age))



class student(people):
	grade = ''
	def __init__(self,n,a,w,g):
		people.__init__(self,n,a,w)
		self.grade = g
	def speak(self):
		print("%s说,我今年%s岁了，上%s年级啦~" % (self.name,self.age,self.grade))


x = student("ken",'10','2','五')
x.speak()
