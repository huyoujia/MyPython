'''
class MusicPlayer(object):


	def __new__(cls):#固定写法
		print("new 方法")

		return super().__new__(cls)#父类的new方法分配内存空间

	def  __init__(self):
		print("you are very cute")


a = MusicPlayer()
'''

#单例练习
class MusicPlayer(object):

	#count= 0
	instance = None
	#init_flag = False
	def __new__(cls):
		if cls.instance is None:
			cls.instance = super().__new__(cls)
		return cls.instance

	def __init__(self):
		#if not MusicPlayer.init_flag:
		self.name = "胡宥嘉"
		print(self.name)
			#MusicPlayer.init_flag = True
b = MusicPlayer()
a = MusicPlayer()
#print(a.name)
#a.name = "小白"
#print(b.name)

