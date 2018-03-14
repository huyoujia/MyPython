import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,480,700)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
	def __init__(self, image_name, speed=1):
		super().__init__()
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.y += self.speed

class BackGround(GameSprite):
	def __init__(self,is_alt=False):
		image_name = "./images/background.png"
		super().__init__(image_name)
		if is_alt:
			self.rect.y = -self.rect.height
	def update(self):
		super().update()

	#判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕上方
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height
		


#英雄类
class Hero(GameSprite):
	def __init__(self):
		super().__init__("./images/life.png",0)
		# 设置初始位置
		self.rect.centerx = SCREEN_RECT.centerx + 100 
		self.rect.bottom = SCREEN_RECT.bottom - 50

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		# 创建子弹精灵组
		self.bullets = pygame.sprite.Group()
	def update(self):
		#飞机移动水平
		if self.moving_right == True:
			self.rect.x += 2
		elif self.moving_left == True:
			self.rect.x -= 2
		elif self.moving_up == True:
			self.rect.y -= 2
		elif self.moving_down == True:
			self.rect.y += 2
		#飞机水平移动
		self.rect.x += self.speed
		# 判断屏幕边界
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right

	def fire(self):
		for i in (1,2,3):
			self.bullet = Bullet()
			#设置精灵位置
			self.bullet.rect.bottom = self.rect.y - 15*i
			self.bullet.rect.centerx = self.rect.centerx
			# 将精灵添加到精灵组
			self.bullets.add(self.bullet)
		


#敌机类
class Enemy(GameSprite):
	def __init__(self):
		#1调用父类方法，创建敌机精灵，并且指定敌机图像
		super().__init__("./images/enemy1.png")
		#2设置敌机初始速度 随机初始速度1-3
		self.speed = random.randint(1,3)
		#3设置敌机随机初始位置
		self.rect.bottom = 0
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)
		
	
	def update(self):
		#1 调用父类方法 让敌机在垂直方向运动
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			print("敌机飞出屏幕")
			self.kill()


# 子弹类
class Bullet(GameSprite):
	def __init__(self):
		super().__init__("./images/bullet1.png",-2)

	def update(self):
		super().update()

# 判断是否超出屏幕 如果是 从精灵组删除
		if self.rect.bottom < 0:
			self.kill()

#定义第二个英雄类
class Hero2(GameSprite):
	def __init__(self):
		super().__init__("./images/life.png",0)
		# 设置初始位置
		self.rect.centerx = SCREEN_RECT.centerx - 100
		self.rect.bottom = SCREEN_RECT.bottom - 50

		self.moving_d = False
		self.moving_a = False
		self.moving_w = False
		self.moving_s = False
		# 创建子弹精灵组
		self.bulletsa = pygame.sprite.Group()
	def update(self):
		#飞机移动水平
		if self.moving_d == True:
			self.rect.x += 2
		elif self.moving_a == True:
			self.rect.x -= 2
		elif self.moving_w == True:
			self.rect.y -= 2
		elif self.moving_s == True:
			self.rect.y += 2
		#飞机水平移动
		self.rect.x += self.speed
		# 判断屏幕边界
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right

	def fire(self):
		for i in (1,2,3):
			self.bullet2 = Bullet()
			#设置精灵位置
			self.bullet2.rect.bottom = self.rect.y - 15*i
			self.bullet2.rect.centerx = self.rect.centerx
			# 将精灵添加到精灵组
			self.bulletsa.add(self.bullet2)
		

