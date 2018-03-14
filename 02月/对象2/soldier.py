import time
class Human(object):
	def __init__(self, name):
		self.name = name
		
	def fire(self,gun):
		gun.shoot()
	
	def add_bullet(self,gun):
		gun.add_bullet(10)


class Gun(object):
	def __init__(self, model):
		self.model = model
		self.bullet_count = 0
	#添加子弹
	def add_bullet(self,count):
		self.bullet_total_count = count
		self.bullet_count += count

	#发射子弹
	def shoot(self):
		if self.bullet_count == 0:
			print("没有子弹，不能发射")
		else:
			print("射击%d/%d"%(self.bullet_count,self.bullet_total_count))
			self.bullet_count -= 1

ak47 = Gun("ak47")
xsd = Human("许三多")
for i in range(30):
	if ak47.bullet_count == 0:
		xsd.add_bullet(ak47)
		print("切换弹夹")
	else:
		time.sleep(0.5)
		xsd.fire(ak47)


'''
class HouseItem(object):
	def __init__(self,name,area):
		self.name = name
		self.area = area

class House(object):
	
	def __init__(self,house_type,house_area):
		self.house_type = house_type
		self.house_area = house_area
		self.free_area = house_area
		#剩余面积默认和总面积一致
		self.furniture = []
	
	def __str__(self):
		return "户型: " + self.house_type + " 总面积: " + str(self.house_area) +" 剩余: " + str(self.free_area) 
	
	def add_item(self,item):
		#判断家具面具是否大于剩余面积
		if item.area > self.house_area:
			print("%s的面积太大，不能添加到房子中"%item.name)
		else:
			#添加家具到列表
			self.furniture.append(item.name)
			#计算剩余面积
			self.free_area -= item.area

bed = HouseItem("席梦思",4)
chest = HouseItem("衣柜",2)
table = HouseItem("餐桌",1.5)

house = House("三室一厅",140)
house.add_item(bed)
house.add_item(chest)
house.add_item(table)
print(house)
print(house.furniture)
'''
