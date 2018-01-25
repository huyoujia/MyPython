'''
class Restaurant(object):
	def __init__(self,restaurant_name,cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type
	def describe_restaurant(self):
		print(self.name)
		print(self.type)
	def open_restaurant(self):
		print("餐馆正在营业")

restaurant = Restaurant("四季酒店","川菜")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant("树树饭店","粤菜")
restaurant2.describe_restaurant()

restaurant3 =Restaurant("峰峰饭店","湘菜")
restaurant3.describe_restaurant()
'''
class User(object):
	def __init__(self,first_name,last_name,age,sex):
		self.name = first_name
		self.name1 = last_name
		self.age = age
		self.sex = sex
	def describe_user(self):
		print(self.name)
		print(self.name1)
		print(self.age)
		print(self.sex)
	def greet_user(self):
		print("hello,dear,打死你个鳖孙儿")

anhuafeng = User("华峰","安",22,"男")
duanjinsong = User("金松","段",22,"男")
jiamiaohao = User("淼浩","贾",18,"男")

anhuafeng.describe_user()
anhuafeng.greet_user()
print("*"*20)
duanjinsong.describe_user()
duanjinsong.greet_user()
print("*"*20)
jiamiaohao.describe_user()
jiamiaohao.greet_user()

