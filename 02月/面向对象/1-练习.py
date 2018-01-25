class Car():
	def __init__(self,newseat,newcolor):
		self.seat = newseat
		self.color = newcolor
	def move(self):
		print("车在移动")
	def stop(self):
		print("车停了")
	
BC = Car(5,"black")
BC.move()
print("奔驰车有%d辆座椅"%BC.seat)
print("奔驰车是%s色"%BC.color)
BC.stop()
print(id(BC))
print("*"*20)

BSJ = Car(4,"white")
BSJ.move()
print("保时捷里有%d个座"%BSJ.seat)
print("保时捷是%s色"%BSJ.color)
BC.stop()
print(id(BSJ))
print("*"*20)
