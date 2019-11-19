#__del__ 魔术方法(析构方法)
'''
	触发时机:当对象被内存回收的时候自动触发[1.页面执行完毕回收所有变量 2.所有对象被del的时候]
    功能：对象使用完毕后资源回收
	参数：一个self接受对象
	返回值：无
'''

class LangDog():
	def __init__(self,name):
		self.name = name
		
	def eatmeat(self):
		print("可爱滴小狼狗{}喜欢吃肉".format(self.name))
		
	def __del__(self):
		print("析构方法被触发")
		
# 1.页面执行完毕回收所有变量
obj = LangDog("迈克尔·蛋蛋")
obj.eatmeat()

#2.所有对象被del的时候
"""
两个不同的变量指向同一个对象,只有把这两个变量都删除了,
这个对象没有变量引用了,才会真正的删除对象.
"""
obj2 = obj
print("==============start==============")
del obj
del obj2
print("==============end==============")

# 3.模拟文件读的操作
fp = open("ceshi.txt", "r",encoding = "utf-8")
res = fp.read()
fp.close()
print(res)
"""
如果有这个文件,就创建一个对象,
"""
import os
class ReadFile():
	# 用来创建对象
	def __new__(cls,name):
		if os.path.exists(name):
			return object.__new__(cls)
			
		return print("没有这个文件")
		
	# 保存文件对象fp 放到对象的成员属性fp当中
	def __init__(self,name):
		# 把文件对象赋值给该对象中的fp成员属性
		self.fp = open("ceshi.txt", "r",encoding = "utf-8")
	
	# 读取文件内容
	def readcontent(self):
		res= self.fp.read()
		return res
		
	# 关闭文件
	def __del__(self):
		self.fp.close()
		
# obj = ReadFile("cesh111222i.txt") error
obj = ReadFile("ceshi.txt")
print(obj)
res = obj.readcontent()
print(res)


































































