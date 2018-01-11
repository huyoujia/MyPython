'''
names = ["huyoujia","zhangyanna","wanghanqing"]
for i in names:
	print(i)
	print("Hi,%s,how are you?"%i)
mode = ["bus","bike","motorcyle","sanlunbike","skate"]
for i in mode:
	print("I want to own my owned %s"%i)
'''

names = ["zhangyanna","wanghanqing","huyoujia"]
for i in names:
	print("%s,我希望你们能和我共进晚餐\n"%i)
print("sorry,huyoujia有事来不了了\n")
names.remove("huyoujia")#胡宥嘉 学习来不了了
names.append("dudengjin")#杜登近 来了
for i in names:
	print("%s,欢迎来到这里\n"%i)
#再邀请三个人
print("欢迎来到这里，玩的开心")
names.insert(0,"zhourunlin")#周润林
names.insert(3,"jiamiaohao")#贾淼浩
names.append("duanjinsong")#段金松
print("现在的嘉宾名单为:%s"% names)
for i in names:
	print("%s欢迎来到这里，玩的开心！\n"% i)
#情况有变，只能邀请两个人参加
print("sorry,计划要改变了，，，\n")
for i in names:
	names.pop()
	if len(names)== 2:
		break
for i in names:
	print("两个人的晚餐 %s" %i)
