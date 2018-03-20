#这个模块放一些常用的工具和基础类和精灵类
#在其他模块调用
import pygame
import random
#设置游戏屏幕大小 这是一个常量
SCREEN_RECT = pygame.Rect(0,0,1100,500)
#敌机的定时器事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

#定制一个精灵类，需要继承pygame提供的精灵类
#需要定义的属性有：
#image图片 
#rect坐标
#speed速度

#接下来开始写敌机方面的内容 产生敌机
#我们还可以定义一个事件常量(发射子弹)
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
	def __init__(self,new_image,new_speed=1):
		super().__init__()
		#图片
		self.image = pygame.image.load(new_image)
		#位置 获取图片的宽和高 get_rect()(0,0,宽，高)
		self.rect = self.image.get_rect()
		#精灵移动的速度 包括英雄精灵 背景精灵 敌机精灵 子弹精灵
		self.speed = new_speed

	def update(self):
		#默认水平方向移动 
		self.rect.x -= self.speed
		#self.rect.x += 1
#以上是游戏的基础类，接下来设置背景类
#明确背景类继承自游戏的精灵类
class Background(GameSprite):
	def __init__(self,is_alt = False):
		#is_alt判断是否为另一张图像
		#False表示第一张图像
		#Ture表示另外一张图像
		#两张图像交替循环
		#传图片
		super().__init__("/home/liutingting/下载/beijing.png")
		if is_alt:
			#如果是第二张图片 初始位置为-self.rect.height
			self.rect.left = -self.rect.width
	#def __init__(self,new_image):
	#	super().init__(new_image)
	def update(self):
		#调用父类方法
		super().update()
		if self.rect.x <=  -self.rect.width:
			self.rect.left = self.rect.width

#敌机出场
class Enemy(GameSprite):
	#敌机精灵
	def __init__(self):
		#1 调用父类方法 创建敌机精灵 并且指定敌机图像
		super().__init__("/home/liutingting/桌面/images/enemy1.png")

		#2 设置敌机的随机初始速度1~3
		self.speed = random.randint(2,5)
		#3 设置敌机的随机初始位置
		self.rect.x = SCREEN_RECT.width + self.rect.width
		max_ = SCREEN_RECT.height -self.rect.height
		self.rect.y = random.randint(0, max_)


	def update(self):
		#1 调用父类方法 让敌机在垂直方向运动
		super().update()
		#判断敌机是否飞出屏幕  如果飞出屏幕将敌机从精灵组删除
		if self.rect.left <=0 :
			self.kill()


#英雄出场
class Hero(GameSprite):
	def __init__(self):
		super().__init__("/home/liutingting/桌面/images/me1.png",0)
		#初始位置
		self.rect.centery = SCREEN_RECT.centery
		self.rect.left = SCREEN_RECT.y-20
		self.move = True
		#子弹精灵组
		self.bullet = pygame.sprite.Group()

	def update(self):
		#super().update()
		#控制飞机移动
		if not self.move:
			self.rect.x += self.speed
		else:
			self.rect.y += self.speed

		#self.rect.y += self.speed
		#飞机不能飞出屏幕
		#不能飞出上方
		if self.rect.y <= 0:
			self.rect.y = 0
		#不能飞出左边
		if self.rect.x <= 0:
			self.rect.x = 0
		#不能飞出下边
		if self.rect.bottom >= SCREEN_RECT.height:
			self.rect.bottom = SCREEN_RECT.height
		#不能飞出右边
		if self.rect.x >= SCREEN_RECT.width:
			self.rect.x = SCREEN_RECT.width
	def fire(self):
		#print("发射子弹")

		for i in (1,2,3):
			bullet = Bullet()
			bullet.rect.left = self.rect.right+i*20
			bullet.rect.centery = self.rect.centery
			self.bullet.add(bullet)


#子弹精灵
class Bullet(GameSprite):

	def __init__(self):
		super().__init__("/home/liutingting/桌面/images/bullet1.png")
	def update(self):
		self.rect.x += 10

		#判断是否超出屏幕 如果是 从精灵组删除
		if self.rect.left >= SCREEN_RECT.width:
			self.kill()




