# ### property 装饰器
'''
功能:可以把类中的方法变成属性
作用:控制该属性的 获取, 设置 ,删除 的操作

@property 用来获取值
@自定义名.setter  用来设置值
@自定义名.deleter 用来删除值
'''
# 方法一
class MyClass():
	def __init__(self,name):
		self.name = name

	@property
	def username(self):
		return self.name
		# pass
		
	@username.setter
	def username(self,val):
		# self.name = val
		pass
		
	@username.deleter
	def username(self):
		# del self.name
		pass

obj = MyClass("小芳")
# res = obj.username()
# print(res)
# 获取username 属性
# print(obj.username)

# 设置username 属性
# obj.username = "小文"
# print(obj.username)

# 删除username 属性
del obj.username
print(obj.username)


# 方法二 (推荐)
print("<====>")
class MyClass():
	def __init__(self,name):
		self.name = name


	def getusername(self):
		return self.name
		# pass

	def setusername(self,val):
		self.name = val
		# pass
		

	def delusername(self):
		del self.name
		# pass
	
	# 按照顺序传参 :  获取 =>  设置 => 删除
	username  = property(getusername,setusername,delusername)
	address  =  property(getusername,setusername,delusername)

obj = MyClass("小芳")
# 获取username
print(obj.username)

# 设置username 属性
obj.username = "小刘"
print(obj.username)

# 删除username 属性
# del obj.username
# print(obj.username)

print(obj.address)

