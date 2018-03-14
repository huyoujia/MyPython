'''
class People(object):
	country = 'china'
	
	@classmethod
	def getCountry(cls):
		return cls.country

hu = People()
print(hu.getCountry())
print(People.getCountry())
'''

class Car(object):
	Count = 10 # 类属性
	@classmethod  #类方法 
	def move(cls):#后面必须传参数
		print("车在移动")
	@staticmethod
	def run():
		print("车在奔跑")#类属性能用类名来调动

	def __init__(self):
		self.color = "蓝色" #实例属性
	
print(Car.Count) #类属性能用类名来调动
Car.move() #类方法直接用类名来调用
