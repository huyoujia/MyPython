
class User(object):
	"""对象的属性"""
	def __init__(self,first_name,last_name,age,sex,login_attempts):
		self.name = first_name
		self.name1 = last_name
		self.age = age
		self.sex = sex
		self.login_attempts= login_attempts

	"""递增  方法"""
	def increment_login_attempts(self):
		self.login_attempts = self.login_attempts + 1

	"""归零 方法"""
	def reset_login_attempts(self):
		self.login_attempts = 0
		

	def describe_user(self):
		print(self.name)
		print(self.name1)
		print(self.age)
		print(self.sex)
	def greet_user(self):
		print("hello,dear,打死你个鳖孙儿")

anhuafeng = User("华峰","安",22,"男",1)
#duanjinsong = User("金松","段",22,"男")
#jiamiaohao = User("淼浩","贾",18,"男")

anhuafeng.describe_user()
anhuafeng.greet_user()
anhuafeng.increment_login_attempts()
print(anhuafeng.login_attempts)

anhuafeng.increment_login_attempts()
print(anhuafeng.login_attempts)#递增

anhuafeng.reset_login_attempts()#归零
print(anhuafeng.login_attempts)
print("*"*20)
#duanjinsong.describe_user()
#duanjinsong.greet_user()
#print("*"*20)
#jiamiaohao.describe_user()
#jiamiaohao.greet_user()

