class Plane():
	# 公有成员属性
	captain = "王铁杵"
	# 私有成员属性
	__air_sister = 20
	
	# 公有绑定方法
	def fly(self):
		print("飞机会飞")
	
	# 公有普通方法 => 只能使用类来调用
	def fly2():
		print("灰机会飞2")

'''
类只有一个,而对象可以实例化多个
多个对象都可以访问类中的公有成员属性方法
而类无法访问对象中的成员
对象和对象之间彼此独立,资源不共享.
对象可以调用类中公有成员,有使用权,没有归属权(不能修改或者删除)
'''

# (1)定义的类访问公有成员属性和方法
print(Plane.captain)
# print(Plane.__air_sister) 私有的成员在类外吊用不了
Plane.fly2()

# 普通方法对象无法调用,因为形参实参不匹配
# obj = Plane()
# obj.fly2()


# (2)定义的类动态添加公有成员属性和方法
Plane.logo = "播音747"
print(Plane.logo)	
res = Plane.__dict__
print(res)

# (1) 添加无参方法
def fashe():
	print("飞机可以当成炮弹发射")
	
Plane.fashe = fashe
Plane.fashe()
	
# (2) 添加有参方法
def wurenjiashi(something):
	print("飞机可以"+something)

Plane.wurenjiashi = wurenjiashi
Plane.wurenjiashi("无人驾驶")

# (3) 通过lambda表达式添加方法
Plane.kongbuxiji = lambda : print("飞机可以用来恐怖袭击,炸五角大楼")
Plane.kongbuxiji()

print(Plane.__dict__)

obj2 = Plane()
print(obj2.__dict__)
obj2.fly()









