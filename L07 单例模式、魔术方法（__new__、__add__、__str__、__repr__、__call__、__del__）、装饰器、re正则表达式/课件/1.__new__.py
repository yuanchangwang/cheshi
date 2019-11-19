# ### __new__ 魔术方法
'''
	触发时机：实例化类生成对象的时候触发(触发时机在__init__之前)
	功能：控制对象的创建过程
	参数:至少一个cls接受当前的类,其他根据情况决定
	返回值：通常返回对象或None
'''
"""
对象.属性
对象.方法()

类.属性
类.方法()
"""
# (1) 基本用法
class MyClass2():
	ccc = 4
obj2 = MyClass2()


class MyClass():
	abc = 123
	def __new__(cls):
		print(cls)
		print(123)
		#要借助父类object中的__new__来创建对象.
		# obj = object.__new__(cls)
		# return obj  # 返回本类对象
		# return None # 返回一个空对象
		return obj2   # 返回一个其他类的对象


# 实例化对象 类的实例化
obj = MyClass()
print(obj)
# print(obj.abc)
print(obj.ccc)

# (2) 对比__new__ 和 __init__ 两个魔术方法的区别
class Boat():

	# def __new__(cls,name):
	def __new__(cls,*args,**kwargs):
		print(1)
		return object.__new__(cls)
		# return None

	# def __init__(self,name):
	def __init__(self,*args,**kwargs):
		# print(2)
		# self.name = name
		strvar = ""
		for i in args:
			strvar += i + " "
		print(strvar)
		print(kwargs)
"""
__new__ 的触发时机要快于 __init__
__new__  是用来创建对象的
__init__ 是用来初始化对象的

先的有对象
才能初始化对象

new 和 init 他门的参数要保持一致.
"""


obj = Boat("周杰伦","李宇春","周星驰",name="韩庚")
# print(obj)


# (3) 如果__new__魔术方法返回的时其他类的对象,不会触发__init__ 本类的魔术方法
class MyClass():
	def __new__(cls,*args,**kwargs):
		# return object.__new__(cls)
		return obj2
		
	def __init__(self,name):
		print(111)

obj = MyClass("你好")



















