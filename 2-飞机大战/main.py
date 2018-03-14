import pygame
import test
class PlaneGame(object):
	def __init__(self):
		print("游戏初始化")
		#1 游戏窗口 2 游戏时钟 3 精灵和精灵组的创建	

		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		self.__create_sprites()

	def start_game(self):
		print("开始游戏")
		while True:
			self.clock.tick(60)
			#事件监听
			self.__event_handler()
			#碰撞检测
			self.__check_collide()
			#更新精灵组
			self.__update_sprites()
			#更新屏幕显示
			pygame.display.update()

	def __create_sprites(self):
		pass

		
	def __event_handler(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()		
	def __check_collide(self):
		pass

	def __update_sprites(self):
		pass
if __name__ == "__main__":
	game = PlaneGame()
	game.start_game()

			
