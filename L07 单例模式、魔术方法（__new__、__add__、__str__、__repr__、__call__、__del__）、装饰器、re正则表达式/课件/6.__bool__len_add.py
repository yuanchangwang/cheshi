# ### __bool__ 魔术方法
'''
	触发时机：使用bool(对象)的时候自动触发
	功能：强转对象
	参数：一个self接受当前对象
	返回值：必须是布尔类型
'''
'''
类似的还有如下等等(了解):
	__complex__(self)      被complex强转对象时调用
	__int__(self)          被int强转对象时调用
	__float__(self)        被float强转对象时调用
	...
	...
'''
class MyClass():
	def __bool__(self):
		return False
		# return 1 error

obj = MyClass()
res = bool(obj)
print(res)



#__add__ 魔术方法  (与之相关的__radd__ 反向加法)
'''
	触发时机：使用对象进行运算相加的时候自动触发
	功能：对象运算
	参数：二个对象参数
	返回值：运算后的值
'''
'''
类似的还有如下等等(了解):
	__sub__(self, other)           定义减法的行为：-
	__mul__(self, other)           定义乘法的行为：
	__truediv__(self, other)       定义真除法的行为：/
	...
	...
'''
class MyClass1():
	def __init__(self,num):
		self.num = num
		
	# self 自动接收对象,other是另外一个值
	# 当对象在+加号左侧的时候,自动触发
	def __add__(self,other):	
		return self.num  * 3 + other
	# 当对象在+加号右侧的时候,自动触发
	def __radd__(self,other):
		return self.num*2+other
"""
obj = MyClass1(5) 
self.num = 5 

当对象在加号左侧的时候触发
obj 被add self 这个参数收走
2 被 add  other 这个参数收走
self.num = 5
other = 2
5 * 3 + 2 = 17
"""
# (1) 对象在加号的左侧
a = MyClass1(5)
res = a + 2
print(res)

# (2) 对象在加号的右侧
"""
self.num = 3
触发__radd__
self 接收对象b  other接收3
self.num * 2 + other = 3 * 2 + 3 = 9
"""
b = MyClass1(3)
res = 3 + b
print(res)

# (3) 对象 + 对象 
res = a + b
print(res)

"""
因为a对象在加号的左侧,先执行add方法
res = a + b
self 接收的是a对象,other接收的时b对象
return self.num + other = a.num*3 + b = 15 + b
res = 15 + b
对象b在加号的右侧 , 触发radd 魔术方法
self 接收对象b  other 接收15
self.num + other => b.num + other = > 3* 2 + 15 = 21
return 21
res = 21
"""


# ### __len__  魔术方法
'''
	触发时机：使用len(对象)的时候自动触发 
	功能：用于检测对象中或者类中成员个数
	参数：一个self接受当前对象
	返回值：必须返回整型
'''
# 给你一个对象,算出该对象所归属的类里面有几个自定义成员.
listvar = [1,2,3,4,5]
res = len(listvar)
print(res)

class MyClass():
	pty1 = 1
	pty2 = 2
	__pty3 = 3
	__pty4 = 4
	
	def func():
		pass 
	def func2():
		pass
	def __func3():
		pass
	def __func4():
		pass
		
	def __len__(self):
		res = MyClass.__dict__
		lst = [i for i in res if not  ( i.startswith("__") and i.endswith("__"))   ]
		# print(lst)
		return len(lst)
	
res = MyClass.__dict__
obj  = MyClass()
res = len(obj)
print(res)
'''
{
'__module__': '__main__', 
'pty1': 1, 'pty2': 2,
 '_MyClass__pty3': 3, 
 'func': <function MyClass.func at 0x0000024C386C9D08>, 
 'func2': <function MyClass.func2 at 0x0000024C386C9D90>, 
 '_MyClass__func3': <function MyClass.__func3 at 0x0000024C386C9E18>, 
 '__dict__': <attribute '__dict__' of 'MyClass' objects>, 
 '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, 
 '__doc__': None
}

'''





















































