import pygame
from plane_sprites import *
#初始化方法
pygame.init()
#创建游戏屏幕
screen = pygame.display.set_mode((480,700))
clock = pygame.time.Clock()
i = 0
#英雄的初始位置
hero_rect = pygame.Rect(200,500,102,126)

#while True:
	#pass
#加载图片
enemy1 = GameSprite("./images/background.png")
enemy2 = GameSprite("./images/me2.png",2)
enemy2.rect.x = 200
enemy_group = pygame.sprite.Group(enemy1,enemy2)
while True:
#绘制到屏幕上
	hero_rect.y -= 1
	if hero_rect.bottom <= 0:
		hero_rect.y = 700
	screen.blit(enemy1,(0,0))
	#screen.blit(bg,(200,500))
	screen.blit(enemy2,hero_rect)
	clock.tick(60)
	
	print(i)
			
	i += 1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("退出游戏")
			exit()
		
enemy_group.update()
enemy_group.draw(screen)
#刷新屏幕
pygame.display.update()
pygame.quit()
