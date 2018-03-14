class Game(object):
	#用类属性定义游戏最高分
	top_score = 100

	@staticmethod
	def show_help():
		print("查看帮助")

	@classmethod  #类方法显示最高分
	def show_top_score(cls):
		print("游戏最高分是%d"%cls.top_score)

	def __init__(self,name):
		self.name = name

	def start_game(self):
		print("开始游戏")


xh = Game("小红")
Game.show_top_score()
Game.show_help()