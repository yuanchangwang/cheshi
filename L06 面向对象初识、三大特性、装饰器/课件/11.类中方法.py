# ### 类中的方法
'''
(1) 普通方法
(2) 绑定方法
	1.绑定到对象 (自动传递对象参数)
	2.绑定到类   (自动传递类参数)
(3) 静态方法 (无论类还是对象,都可以调用)
'''
class Dog():
	food = "骨头"
	def __init__(self,name):
		self.name = name
		
	# 绑定方法 (绑定到对象)
	def tian(self):
		print("小狗都喜欢舔主任")
		# print("小狗都喜欢舔主任",self.name)
		
	# 普通方法
	def jiao():
		print("小狗会旺旺旺的交换")
		
	# 绑定方法 (绑定到类)
	@classmethod
	def tail(cls):
		print(cls)
		print(cls.food)
		print("小狗会摇尾巴")
		
	# 静态方法 (对象,类都能调用)
	@staticmethod
	def jump():
		print("小狗喜欢抓飞盘")
	
obj = Dog("詹姆斯旺")
# 普通方法的调用 (只能使用类来调用,因为没有参数)
# Dog.jiao()
# obj.jiao() # error self 系统会默认传递,但是新参没有,不能一一对应

# 绑定到对象方法的调用
# obj.tian()
# Dog.tian(111111)  如果函数体里用到了该对象,类名调用的方式不可以.

# 绑定到类方法的调用
# Dog.tail()
# obj.tail() # 先把obj所归属的类找出来,然后把该类当成参数进行传递.

# 静态方法的调用 (对象,类都能调用)
obj.jump()
Dog.jump()











