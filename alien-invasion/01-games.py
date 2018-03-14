import pygame
from plane_sprites import *
pygame.init()
pygame.mixer.music.load('./music/bgm.mp3')
pygame.mixer.music.play()


class PlaneGame(object):
	
	def __init__(self):
		"""
		1游戏窗口 2游戏时钟 3创建我的精灵和精灵组
		"""
		print("游戏初始化")
		#初始化窗口 size = width height
		self.screen = pygame.display.set_mode((SCREEN_RECT.width,SCREEN_RECT.height))
		#游戏时钟
		self.clock = pygame.time.Clock()
		#创建精灵和精灵组
		self.__create_sprites()
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
		pygame.time.set_timer(HERO_FIRE_EVENT,500)
		
	def start_game(self):
		print("开始游戏")
		while True:
			#1刷新帧率
			self.clock.tick(60)
			#2监听事件
			self.__handler_event()
			#3碰撞检测
			self.__check_collide()
			#4更新精灵和精灵组 相当于原来的bilt绘制
			self.__update_sprites()
			#5刷新屏幕
			pygame.display.update()
		

	def __create_sprites(self):
		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)
		self.hero2 = Hero2()
		self.hero2_group = pygame.sprite.Group(self.hero2)
		#self.back_group = pygame.sprite.Group()
		self.enemy = Enemy()
		self.enemy_group = pygame.sprite.Group()

		bg1 = BackGround()
		bg2 = BackGround(True)
		self.back_group = pygame.sprite.Group(bg1,bg2)


		
			
	def __handler_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				#卸载pygame 退出程序
				self.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				new_enemy = Enemy()
				self.enemy_group.add(new_enemy)
				print("敌机出场....")
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.hero.moving_right = True
				elif event.key == pygame.K_LEFT:
					self.hero.moving_left = True
				elif event.key == pygame.K_UP:
					self.hero.moving_up = True
				elif event.key == pygame.K_DOWN:
					self.hero.moving_down = True
				if event.key == pygame.K_d:
					self.hero2.moving_d= True
				elif event.key == pygame.K_a:
					self.hero2.moving_a = True
				elif event.key == pygame.K_w:
					self.hero2.moving_w = True
				elif event.key == pygame.K_s:
					self.hero2.moving_s = True



			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.hero.moving_right = False
				elif event.key == pygame.K_LEFT:
					self.hero.moving_left = False
				elif event.key == pygame.K_UP:
					self.hero.moving_up = False
				elif event.key == pygame.K_DOWN:
					self.hero.moving_down = False
				if event.key == pygame.K_d:
					self.hero2.moving_d= False
				elif event.key == pygame.K_a:
					self.hero2.moving_a = False
				elif event.key == pygame.K_w:
					self.hero2.moving_w = False
				elif event.key == pygame.K_s:
					self.hero2.moving_s = False
	




			elif event.type == HERO_FIRE_EVENT:
				self.hero.fire()
				self.hero2.fire()
	@staticmethod
	def __game_over():
		print("游戏结束")
		pygame.quit()
		exit()

				
				
	def __check_collide(self):
		# 子弹摧毁敌机
		pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
		#  敌机摧毁英雄
		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		#判断列表时候有内容
		if len(enemies) >0:
			self.hero.kill()
			PlaneGame.__game_over()	
	def __update_sprites(self):
		for i in [self.back_group,self.hero_group,self.hero2_group,self.enemy_group,self.hero.bullets,self.hero2.bulletsa]:
			i.update()
			i.draw(self.screen)
		
	
if __name__ == "__main__":
	#使用游戏类 创建一个游戏对象
	game = PlaneGame()
	#开始游戏
	game.start_game()

