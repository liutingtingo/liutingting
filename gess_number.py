import random

class Liu_tingting(object):
	def __init__(self):
		self.cai_times = 0
		self.score =0
		self.int = 0
	def liutt_gess(self):
		self.int = random.randint(1, 99)
		self.cai_times +=1
		 		
		while True:
			self.cai_times +=1
			self.score +=1
			T = int(input("请输入一个1～99的数字"))
			if T > self.int:
				print("猜大了，再试试吧")
			
			elif T < self.int:
				print("猜小了,再试试吧")
			else:
				print("哇，好棒！猜中了")
				break
			print("一共得了%d分"%self.score)
			print("本局共猜了%d次"%self.cai_times)
liutingting_playgame = Liu_tingting()

while True:
	liutingting_start = int(input("1.开始游戏 2.退出"))
	if liutingting_start == 1:
		liutingting_playgame.Liu_tingting()
	if liutingting_start == 2:
		break
	