#coding:utf-8
import pygame
from pygame.locals import *
import time
import random
'''
1、搭建界面  主要完成窗口和背景图的显示
2、显示控制玩具飞机
3、优化代码  优化发射子弹
4、让敌机移动
'''

#使用面向对象的方式显示飞机  以及控制其左右移动
class HeroPlane(object):
	def __init__(self, screen):
		self.screen = screen
		self.x = 130
		self.y = 400

		#设置保存飞机需要的图片名字
		self.imageName = "./feiji/hero.gif"
		
		# 根据名字生成飞机图片
		self.image = pygame.image.load(self.imageName).convert()

		# 用来保存飞机发射出的所有子弹
		self.bulletList = []	

	def display(self):
		# 更新飞机的位置
		self.screen.blit(self.image,(self.x,self.y))	

		# 用来存放需要删除的对象信息
		needDelItemList = []

		for i in self.bulletList:
			if i.judge():
				needDelItemList.append(i)

		# 删除self.bulletList中需要删除的对象		
		for i in needDelItemList:
			self.bulletList.remove(i)

		# 更新这架飞机发射出的所有子弹的位置
		for bullet in self.bulletList:
			bullet.display()
			bullet.move()

	def moveLeft(self):
		self.x -= 10

	def moveRight(self):
		self.x += 10

	def sheBullet(self):
		newBullet = Bullet(self.x,self.y,self.screen)
		self.bulletList.append(newBullet)


class Bullet(object):
	def __init__(self, x,y,screen):
		self.x = x + 40
		self.y = y - 50
		self.screen = screen
		self.image = pygame.image.load("./feiji/bullet-3.gif").convert()


	def move(self):
		self.y -= 2

	def display(self):
		self.screen.blit(self.image,(self.x,self.y))

	def judge(self):
		if self.y < 0:
			return True
		else:
			return False

# 定义敌机类
class EnemyPlane(object):
	def __init__(self, screen):
		# 设置敌机默认位置
		self.x = 0
		self.y = 0
		# 设置要显示的内容
		self.screen = screen

		# 设置飞机默认位置
		self.x = 0
		self.y = 0

		self.imageName = "./feiji/enemy-1.gif"
		self.image = pygame.image.load(self.imageName).convert()

		# 用来存储敌人飞机发射的所有子弹
		self.bulletList = []

		# 默认开始方向
		self.direction = "right"

	def display(self):
		# 更新飞机的位置
		self.screen.blit(self.image,(self.x,self.y))

		#存放需要删除的对象信息
		needDelItemList = []

		for i in self.bulletList:
			if i.judge():
				needDelItemList.append(i)

		for i in needDelItemList:
			self.bulletList.remove(i)

		# 更新这架飞机发射出的所有子弹位置
		for bullet in self.bulletList:
			bullet.display()
			bullet.move()


	def move(self):
		# 如果碰到了右边的边界  那么就往左走，如果碰到了左边的边界  那么就忘右走
		if self.direction == "right":
			self.x += 2
		elif self.direction == "left":
			self.x -= 2


		if self.x > 360 -50:
			self.direction = "left"
		elif self.x < 0:
			self.direction = "right"

	# 敌机发射子弹
	def sheBullet(self):
		num = random.randint(1,100)
		if num == 88:
			newBullet = EnemyBullet(self.x,self.y,self.screen)
			self.bulletList.append(newBullet)

# 敌机发射子弹
class EnemyBullet(object):
	def __init__(self, x,y,screen):
		self.x = x + 30
		self.y = y + 30
		self.screen = screen
		self.image = pygame.image.load("./feiji/bullet-1.gif").convert()

	def move(self):
				self.y += 2


	def display(self):
					self.screen.blit(self.image,(self.x,self.y))

	def judge(self):
			if self.y > 560:
					return True
			else:
				return False	
		
if __name__ == '__main__':
	# 创建一个窗口  用来显示内容
	screen = pygame.display.set_mode((360,560),0,32)

	# 创建一个和窗口大小的图片  用来显示背景
	background = pygame.image.load('./feiji/background.png').convert()

	# 创建一个玩具飞机的图片
	# hero = pygame.image.load("./feiji/hero.gif").convert()
	heroPlane = HeroPlane(screen)

	# 创建一个敌人飞机
	enemyPlane = EnemyPlane(screen)

	# 用来保存飞机的x，y坐标
	x = 0
	y = 0
	# 把图片放到背景中去显示
	while True:
		# 设定需要显示的背景图
		screen.blit(background,(0,0))
		# 设置要显示的飞机图片
		# screen.blit(hero,(x,y))
		heroPlane.display()

		enemyPlane.display()
		enemyPlane.move()
		enemyPlane.sheBullet()

		# 获取事件
		for event in pygame.event.get():
			# 判断是否惦记了退出按钮
			if event.type == QUIT:
				print("exit")
				exit()
			# 判断是否按下了健
			elif event.type == KEYDOWN:
				if event.key == K_a or event.key == K_LEFT:
					print("left")
					# 控制飞机让其向左移动
					heroPlane.moveLeft()
				elif event.key == K_d or event.key == K_RIGHT:
					print("right")
					# 控制飞机向右移动
					# x += 5
					heroPlane.moveRight()
				elif event.key == K_SPACE:
					print("space")
					heroPlane.sheBullet()

		#通过延时的方式，来降低这个while循环的循环速度，从而降低了cpu的占用率
		time.sleep(0.01)

		# 更新要显示的内容
		pygame.display.update()