import time
class xu(object):
	def __init__(self,name):
		self.name=name
		self.gun=None
	def fire(self,gun):
		gun.shoot()


class Gun(object):
	def __init__(self,model):
		self.model=model
		self.bullet_count = 0
	def add_bullet(self,count):
		self.bullet_count+=count
	def shoot(self):
		if self.bullet_count==0:
			print('没有子弹')
		else:
			self.bullet_count-=1
			print('发射子弹',self.bullet_count,'哒哒哒')

a=xu('斯沃特')
s=Gun('加特林')
s.add_bullet(1000)
for i in range(500):
	time.sleep(0.05)
	a.fire(s)
