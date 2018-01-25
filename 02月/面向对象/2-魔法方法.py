class Car:
	def __init__(self,color):
		self.color = color
	def __str__(self):
		info = "你开的是玛莎拉蒂"
		return info
msld = Car("color")
print(msld)
