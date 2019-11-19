# ### 单态模式
"""
无论实例化类几次,都有且只有一个对象.为了节省内存空间
"""
# (1) 基本用法
class Singleton():
	__obj = None
	def __new__(cls):
		if cls.__obj is None:
			obj  = object.__new__(cls)
			cls.__obj = obj
		return cls.__obj 

obj1 = Singleton()
print(obj1)
obj2 = Singleton()
print(obj2)
obj3 = Singleton()
print(obj3)

# (2) 实际的含义,对象和init之间的关系
class Singleton():
	__obj = None
	def __new__(cls,name):
		if cls.__obj is None:
			cls.__obj = object.__new__(cls)
		return cls.__obj
		
	def __init__(self,name):
		self.name = name
		
obj1 = Singleton("张三丰")
obj2 = Singleton("李三丰")
print(obj1.name)
print(obj2.name)



























