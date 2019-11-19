# ### #__call__ 魔术方法
'''
	触发时机：把对象当作函数调用的时候自动触发
	功能: 模拟函数化操作
	参数: 参数不固定,至少一个self参数
	返回值: 看需求
'''

# (1) 基本用法
class MyClass():
	def __call__(self):
		print("call 方法被调用")
	# pass
		
obj  = MyClass()
obj() # 把对象当成函数进行调用,自动触发__call__

# (2) 模拟做蛋糕的过程,,利用call 方法进行统一的调用
class MakeCake():
	# def __init__(self,something):
		
	# self 系统自己给你传,但是something 需要你手动填写 , 形参实参一一对应
	def __call__(self,something):
		self.something = something
		print("这是我的{}方法:".format(self.something))
		self.step1()
		self.step2()
		self.step3()
		
		
	def step1(self):
		print("把鸡蛋打碎,把面粉家里面,搅拌一下")
		
	def step2(self):
		print("把盆里的面扔到锅里蒸一下")
	
	def step3(self):	
		print("把面从锅里面拿出来,开始吃")
		
		
obj = MakeCake()
# 普通写法 累赘
# obj.step1()
# obj.step2()
# obj.step3()
# 调用魔术方法__call__ 优化代码
obj("做蛋糕")


# (3) 模拟内置int强转方法 myint

# 整型 布尔型 浮点型 存数字字符串
import math
class MyInt():
	# sign 代表符号,默认正值
	def myfunc(self,strvar,sign = 1):	
		isnull = strvar.lstrip("0")
		# 判断是否处理完的字符串是不是空的,如果是空的,这个串是"0000.."
		if isnull == "":
			return 0
		res = eval(strvar) * sign		
		return res
		
	def __call__(self,num):

		if isinstance(num,bool):	
			if num == True:
				return 1
			else:
				return 0 
				
		elif isinstance(num,int):
			return num
			
		elif isinstance(num,float):
			if num < 0 :
				return math.ceil(num)
			else:
				return math.floor(num)
				
		elif isinstance(num,str):
		
			#num[1:] 从第二个字符往后所有的字符串全截取出来
			if (num[0] == "+" or num[0] == "-") and num[1:].isdecimal():
				if num[0] == "+":
					sign = 1
				else:
					sign = -1
				# 数字和符号实际上是分开处理的 
				return self.myfunc(num[1:],sign)
				
			elif num.isdecimal():	
				return self.myfunc(num)

			'''
			# 判断纯数字
			if num.isdecimal():
				# self.myfunc(num)
				"""
				res = eval(num)
				return res
				"""
			'''
		else:
			return "对不器,处理不了这个数据类型"
	
	
myint = MyInt()
print(myint(True))
print(myint(False))

print("<===>")
print(myint(5))

print("<===>")
print(myint(6.9))
print(myint(-6.9))

print("<=112233==>")
print(myint("11122233"),type(myint("11122233")))
# print(myint("00001223"))
print(myint("-11122233"),type(myint("-11122233")))
"""
# 把字符串当成代码来执行;
res=  eval("1234")
print(res)

# ceil
# floor
print(int(-5.1))
print(int(5.1))

5.9
print(math.ceil(5.9))
print(math.floor(5.9))

-5.9
print(math.ceil(-5.9))
print(math.floor(-5.9))


# print(int("+00001223"))
print(int("000000000234"))

# eval执行空值是错误的
res = eval("")

# "0000000"

"""
print(myint([1,2,3,4]))



















