
f = open("2.py","r")

print("*"*20)
print(f.readlines(20))
f.seek(1,0)
print("当前光标位置:",f.tell())

f.close()

