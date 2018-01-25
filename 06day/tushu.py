#借书
def borrow_book():
	name = input("请输入你要借的书的名字")
	id = input("请出示你的借书卡卡号")
	 
	




































title = "图书管理系统"
print(title.center(20,"*"))
list = []
while True:
	fn = int(input("请输入你所选的项 1借书 2还书 3退出"))
	if fn == 1:
		borrow_book()
	elif fn == 2:
		return_book()
	elif fn == 3:
		break
print(list)
