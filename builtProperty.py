#coding:utf-8
class Itcast(object):
	def __init__(self, subject1):
		super(Itcast, self).__init__()
		self.subject1 = subject1
		self.subject2 = "cpp"



	# 属性访问时拦截 。打log
	def __getattribute__(self,obj):
		if obj == "subject1":
			print("log subject1")
			return "redirect python"
		else:
			return object.__getattribute__(self,obj)


	def show(self):
		print("this is itcast")

s = Itcast("python")

print(s.subject1)
print(s.subject2)

print("*"*30)
#__getattribute__存在的坑
class Person(object):
    def __getattribute__(self,obj):
        print("---test---")
        if obj.startswith("a"):
            return "hahha"
        else:
            print("heiheihei")


    def test(self):
        print("heihei")

t = Person()

t.a #返回hahha
t.b #会让程序死掉
        #原因是：当t.b执行时，会调用Person类中定义的__getattribute__方法，但是在这个方法的执行过程中
        #if条件不满足，所以 程序执行else里面的代码，即return self.test  问题就在这，因为return 需要把
        #self.test的值返回，那么首先要获取self.test的值，因为self此时就是t这个对象，所以self.test就是
        #t.test 此时要获取t这个对象的test属性，那么就会跳转到__getattribute__方法去执行，即此时产
        #生了递归调用，由于这个递归过程中 没有判断什么时候推出，所以这个程序会永无休止的运行下去，又因为
        #每次调用函数，就需要保存一些数据，那么随着调用的次数越来越多，最终内存吃光，所以程序 崩溃
        #
        # 注意：以后不要在__getattribute__方法中调用self.xxxx