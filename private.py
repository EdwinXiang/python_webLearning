#coding:utf-8

class Person(object):
	def __init__(self, name,age,taste):
		self.name = name
		self._age = age
		self.__taste = taste


	def showperson(self):
		print(self.name)
		print(self._age)
		print(self.__taste)


	def dowork(self):
		self._work()
		self.__away()

	def _work(self):
		print("my_work")

	def __away(self):
		print("my_away")


class Student(Person):
	def construction(self,name,age,taste):
		self.name = name
		self._age = age
		self.__taste = taste


	def showsudent(self):
		print(self.name)
		print(self._age)
		print(self.__taste)


	@staticmethod
	def testbug():
		_Bug.showbug()


class _Bug(object):
	@staticmethod
	def showbug():
		print("showbug")



s1 = Student("jack",35,"football")
s1.showperson()
print("-"*30)
# s1.showsudent()

print("-"*30)
s1.construction("rose",25,"basketball")
s1.showperson()
print("-"*30)

s1.showsudent()
print("*"*30)

s1.testbug()

		
		