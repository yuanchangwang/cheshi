# ### __str__
'''
	触发时机: 使用print(对象)或者str(对象)的时候触发
	功能:     查看对象信息
	参数:     一个self接受当前对象
	返回值:   必须返回字符串类型
'''
class Cat():
	gift = "抓老鼠"
	def __init__(self,name):	
		self.name = name
		
	def cat_info(self):
		strvar = "这个对象叫{},小猫天生就会{}".format(self.name,self.gift)
		return strvar
		
	def __str__(self):
		return self.cat_info()
		# return 123 如果返回的不是字符串就报错

tom = Cat("汤姆")
# res = tom.cat_info()
# print(res)
# 触发方式一
print(tom)
# 触发方式二
res = str(tom)
print(res)


# ### __repr__
'''
	触发时机: 使用repr(对象)的时候触发
	功能:     查看对象,与魔术方法__str__相似
	参数:     一个self接受当前对象
	返回值:   必须返回字符串类型
'''
class Mouse():
	gift = "会打洞"
	def __init__(self,name):
		self.name = name
	
	def mouse_info(self):
		strvar = "该对象的名字是{},天赋:龙胜龙,凤生凤,老鼠的儿子{}".format(self.name,self.gift)
		return strvar
		
	def __repr__(self):
		return self.mouse_info()
		
	# 在底层系统有赋值操作, 把函数当成变量名使用的一种方式 , 只不过看起来很奇怪,左右各有两个下划线.
	# __str__ = __repr__
		
jerry = Mouse("杰瑞")
res = repr(jerry)
print(res)

print(jerry)
res = str(jerry)
print(res)

print("<====>")
def func():
	print("这是一个函数")
func2 = 5
func2 = func
func2()




















