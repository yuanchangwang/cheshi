# ### 类的封装
class Car():
	# 公有的成员属性
	price = "100万"
	# 私有的成员属性 (由2个下划线开头)
	__oil = "保密"
	
	# 公有的成员方法
	def run(self):
		print("小车跑的快")

	def run2(self,num):
		print(num)
	
	# 私有的成员方法
	def __oil_info():
		print("小车的油耗不告诉你")

'''
绑定方法:
(1) 绑定到对象:自动传参(参数是一个对象)
(2) 绑定到类:  自动传参(参数是一个类)
self 是约定俗成的写法,代表被对象
'''


# 实例化一个对象
obj = Car()


# (1)实例化的对象访问公有成员属性和方法
res  = obj.price
print(res)

obj.run()
obj.run2(15)

# obj.__oil 从这体现出类的封装性

# (2)实例化的对象动态添加公有成员属性
obj.color = "屎黄色"
print(obj.color)

# __dict__ 用dict魔术属性来查看对象的内部成员
print(obj.__dict__)


# 实例化的对象动态添加公有成员方法
# (1) 添加无参方法
def fangxiangpan():
	print("这是制造方向盘的方法")

# obj.fangxiangpan fangxiangpan是自定义的一个名字,是obj动态添加的成员方法
obj.fangxiangpan = fangxiangpan
obj.fangxiangpan()
print(obj.__dict__)

# (2) 添加有参方法
def huibianxing(obj,name):
	print("我的小车,可以变成"+name,"价格是:"+obj.price)
obj.bianxing = huibianxing
# obj.bianxing("hello kitty")
obj.bianxing(obj,"hello kitty")

import types
#MethodType(函数,对象) 把函数绑定到哪个对象上
#绑定成功之后,在调用,系统会自动把这个对象当成参数进行传递
obj.bianxing = types.MethodType(huibianxing,obj)
# obj.bianxing = bianxing
obj.bianxing("hello ketty")


# (3) 通过lambda表达式来进行动态添加
func = lambda : print("我是大黄蜂")
obj.dahuangfeng = func
obj.dahuangfeng()

print(obj.__dict__)
















