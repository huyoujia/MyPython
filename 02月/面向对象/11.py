class Restaurant(object):
	def __init__(self,restaurant_name,cuisine_type):
		self.number_served = 0
		self.name = restaurant_name
		self.type = cuisine_type
		
	def set_number_served(self,number_served):
		self.number_served = number_served

	def describe_restaurant(self):
		print(self.name)
		print(self.type)

	def open_restaurant(self):
		print("餐馆正在营业")

	def increment_number_served(self,num):
		self.num = num + 1
		

restaurant = Restaurant("四季酒店","川菜")
restaurant.set_number_served(3)
print("就餐人数为%s"%restaurant.number_served)
restaurant.increment_number_served(5)
print("我认为这家餐馆每天可能接待的就餐人数:%d"%restaurant.num)
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("*"*20)
restaurant2 = Restaurant("树树饭店","粤菜")
restaurant2.set_number_served(7)
print("就餐人数为%s"%restaurant2.number_served)
restaurant2.increment_number_served(6)
print("我认为这家餐馆每天可能接待的就餐人数:%d"%restaurant2.num)
restaurant2.describe_restaurant()

print("*"*20)
restaurant3 =Restaurant("峰峰饭店","湘菜")
restaurant3.set_number_served(10)
print("就餐人数为%s"%restaurant3.number_served)
restaurant3.increment_number_served(8)
print("我认为这家餐馆每天可能接待的就餐人数:%d"%restaurant3.num)
restaurant3.describe_restaurant()
