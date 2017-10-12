#coding:utf-8
# 装饰器带参数，在原有装饰器的基础上，设置外部变量
from time import ctime,sleep


def timeFun_arg(pre="hello"):
	def timefun(func):
		def wrappedfunc():
			print("%s called at %s %s"%(func.__name__,ctime(),pre))
			return func()
		return wrappedfunc
	return timefun


@timeFun_arg("itcast")
def foo():
	print "I am foo"


@timeFun_arg("python")
def too():
	print("I am too")



foo()
sleep(2)
too()

print("-"*30)
#类装饰器
class Test(object):
	def __init__(self, func):
		print("---初始化---")
		print("func name is %s"%func.__name__)
		self.__func = func

	def __call__(self):
		print("装饰器中的功能")
		self.__func()


@Test
def test():
	print("----test----")

test()


#装饰器中的return
def timefun(func):
	def wrappedfunc():
		print("%s called at %s"%(func.__name__,ctime()))
		return func()
	return wrappedfunc


@timefun
def foo():
		print("I am foo....")	


@timefun
def getInfo():
		return "----hahahaha----"	


foo()
sleep(2)
foo()

print(getInfo())


#被装饰器的函数有参数
def timefun1(func):
	def wrappedfunc(a,b):
		print("%s called at %s"%(func.__name__,ctime()))
		print(a,b)
		func(a,b)
	return wrappedfunc



@timefun1
def foo1(a,b):
	print(a+b)

print("--"*20)
foo1(3,5)
sleep(2)
foo1(2,4)