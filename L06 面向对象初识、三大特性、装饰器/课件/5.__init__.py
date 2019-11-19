#__init__魔术方法(构造方法)
'''
	触发时机：实例化对象,初始化的时候触发
	功能：为对象添加成员
	参数：参数不固定,至少一个self参数
	返回值：无
'''

# (1) 基本用法 (至少有一个参数)
class MyClass():
	def __init__(self):
		self.name = "古永锵"
		
# 实例化对象
obj = MyClass()
print(obj.name)

# (2) 多个参数的__init__ 构造方法
class MyClass():
	def __init__(self,name):
		# self.name  自定义成员属性name
		# self.name = name  等号右边的这个name 是参数传进来的值
		self.name = name
		
# name 这个参数值如何穿进去?
obj = MyClass("中林志")
obj = MyClass("刘鹏")
print(obj.name)

# (3) 综合实例
class Children():

	def __init__(self,name,skin):
		self.name = name
		self.skin = skin

	def eat(self):
		print(self.name + "下生只能喝奶奶")
		
	def drink(self):
		print(self.name + "下生喜欢吃烤肉")
		
	def sleep(self):
		print(self.name + "一天睡23个小时,还有一个小时,尿尿")

	def child_info(self):
		print("这个对象是{},他的肤色是{}".format(self.name,self.skin))

# __init__构造方法,传递参数时,就在实例化类的括号中填写
obj1 = Children("何伟福","黄色")
obj1.eat()
obj1.child_info()

obj2 = Children("龙阳","黑色")
obj2.drink()
obj2.child_info()

obj3 = Children("王宝强","绿色")
obj3.sleep()
obj3.child_info()
'''
类可以是一个,但对象可以实例化出多个
每个对象彼此都是独立的
'''























