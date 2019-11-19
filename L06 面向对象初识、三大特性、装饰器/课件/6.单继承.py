# ### 继承
'''
继承:(1) 单继承 (2)多继承

至少两个类,
一个类继承另外一个类,那么该类是子类(也叫作衍生类)
另外一个,这个被继承的类,叫做父类(也叫作超类)

object 在python中 这个类是所有类的父类
'''
class Human():
	skin = "黝黑"
	hair = "黑色"
	def study(self):
		print("远古人来天生会学习")
		
	def __sex(self):
		print("远古人类的性别是保密了")

# (1) 子父继承之后,子类可以使用父类的公有成员属性方法


# obj = Human()
# print(obj.skin)
# 想让一个类继承另外一个类,语法在定义类的时候,括号里面写(父类)
class Man(Human):
	pass

obj = Man()
print(obj.hair)

# (2) 子父继承之后,子类不能调用父类的私有成员属性方法
'''
无论在子类的内部,还是在类的外部,都无法调用父类的私有成员属性方法.
'''
class Woman(Human):
	def myskill():
		self.__sex()
obj = Woman()
# obj.myskill()
# obj.__sex()


# (3) 子父继承之后,子类可以改写父类的公有方法
'''
如果子类当中含有该方法,那么优先调用子类的方法
如果子类当中不含有该方法,再去调用父类的方法.
有就调用自己的,没有就调用父类的(一定是共有的成员属性方法;)
'''
class Children(Human):
	def study(self):
		print("小孩天生比较灵光,天生可以感知灵异事件.")

# 类的实例化 或者 说 实例化对象
obj = Children()
obj.study()






