# ### 删除类或者对象中的成员
class Car():
	# 公有成员属性
	price  =  "5元"
	# 私有成员属性
	__oil = "涡轮增压发动机,油耗百公里50升111"

	# 公有绑定方法
	def bianxing_dog(self):
		print("我的车可以变成小狗,价格:" ,self.price)
		
	# 公有普通方法
	def bianxing_dog2():
		print("我的车可以变成小狗",Car.price)


	# 私有绑定方法
	def __oil_info(self):
		print("我的油耗信息是222",self.__oil)
		
	# 私有普通方法
	def __oil_info2():
		print("我的油耗信息是222:",Car.__oil)
		
	# 公有方法调用私有成员,用对象来调用
	def oil_info(self):
		print(self.__oil)
		self.__oil_info()
		
	# 也可以用类来调用
	def oil_info2():
		print(Car.__oil)
		Car.__oil_info2()

# 实例化类产生对象obj
obj = Car()


'''
# 当对象去调用方法时,系统会自动把obj当成参数进行传递,
bianxing_dog 中的self自动进行接收
self.price  <==> obj.price 
在类中要么使用对象.属性或者方法  要么使用类.属性或者方法
其他调用情况都是错误的
'''
obj.bianxing_dog()
# print(obj.price)

# 1. 在类外可以调用私有的成员属性方法么?
'''
不行!
可以在类内使用公有方法调用私有成员属性和方法
'''
# obj.__oil_info()
obj.oil_info() # 用对象来调用的方法
Car.oil_info2()# 用类来调用的方法

# 2. 就是想直接调用私有成员,可以么?
'''
私有成员的改名机制:
私有成员的名字 => _类名+私有成员本身
其他语言当中,如果是私有的,无论用什么方式都调用不了.
'''
print(Car._Car__oil)
obj._Car__oil_info()

# 3.删除对象中或者类的成员 用关键字del
'''
price 默认归属于类中的,obj对象可以使用,
但是无权修改或者删除,除非obj当中也有price属性.
'''

# (1)实例化的对象删除公有成员属性和方法
# (2)定义的类删除公有成员属性和方法

# obj.price = 90
# print(obj.__dict__)
# del obj.price

del Car.price
# print(Car.price) # 如果删除了就没有了.

del Car.oil_info
print(Car.__dict__)













