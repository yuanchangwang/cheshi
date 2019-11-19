# ### oop 面向对象程序开发

# (1) 类的定义
class MyClass:
	pass

class MyClass():  #推荐使用
	pass

class MyClass(object):
	pass


# (2) 类的实例化
class MyClass():
	pass
	
# 类的实例化  也可以叫做 实例化对象 obj就是对象
obj = MyClass()


# (3) 类的基本结构
'''
成员属性
成员方法

对象.成员属性
对象.成员方法()
'''
class MyClass():
	# 成员属性
	color = "小汽车的颜色是蓝色的"
	# 成员方法
	def run(self):
		print("小汽车会pao")

# 实例化对象
obj = MyClass()
# 利用对象obj,调用类中的成员属性
print(obj.color)
# 利用对象boj 调用类中的成员方法
obj.run()


class  MyClass():
	if 5==5:
		print("条件成立")
'''
从语法上来看,这样写允许,但是严禁使用,
一般类中只有2样东西,一个试成员属性,一个试成员方法,
除此之外就没有了.
类中的代码,不需要实例化对象,就可以默认从上到下依次执行了.
'''

# (4)类的命名

'''
让别人看代码时,更加读懂语意.
大驼峰命名法: 每个单词首字符都大写  MyCar
小驼峰命名法: 只有第一个单词首字符小写,剩下都大写 myCar
# 命名一个类名的时,推荐使用大驼峰命名法:
'''















