class Home(object):
# 存家具的面积
	def __init__(self,newarea):
		self.area = newarea
		#定义一个列表  容纳
		self.contains = []
	def __str__(self):
		msg = "当前可剩面积为:" + str(self.area)
		if len(self.contains) > 0:
			msg = msg + "容纳的物品有"
			for i in self.contains:
				msg = msg + i.getName() + ","
			msg = msg.strip(",")
		return msg
	"""容纳物品"""
	def accommodate(self,item):
		#如果可用面积大于物品的占用面积
		needArea = item.getUsedArea()
		if self.area > needArea:
			self.contains.append(item)
			self.area -= needArea
			print("已经存放到房间中")
		else:
			print("房间可用面积为:%d,但是当前要存放的物品需要的面积为%d"%(self.area,needArea))		
		
#定义bed类
class Bed(object):
	def __init__(self,area,name = "床"):
		self.name = name
		self.area = area

	def __str__(self):
		msg = "床的面积为:" + str(self.area)
		return msg

	#获取床的占用面积
	def getUsedArea(self):
		return self.area
		
	
	def getName(self):
		return self.name

#创建一个新家对象
hujia = Home(150)
print(hujia)

#创建一个床对象
newbed = Bed(20)
print(newbed)
#把床安放到家里面

hujia.accommodate(newbed)
print(hujia)


	
