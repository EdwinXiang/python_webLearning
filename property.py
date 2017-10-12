#coding:utf-8
class Money(object):
	def __init__(self):
		self.__money = 0



	# def getMoney(self):
		# return self.__money


	# def setMoney(self,value):
		# if isinstance(value,int):
			# self.__money = value
		# else:
			# print("error:不是整形数字")


	# 使用property升级getter和setter方法
	# money = property(getMoney,setMoney)

	#使用property取代getter和setter方法
	@property
	def money(self):
		return self.__money


	@money.setter
	def money(self,value):
		if isinstance(value,int):
			self.__money = value
		else:
			print("error:不是整形数字")

		

a = Money()
print(a.money)
a.money = 100
print(a.money)

# a = money.getMoney()
# print(a)
# money.setMoney(10)
# a = money.getMoney()
# print(a)

# print(money.money)