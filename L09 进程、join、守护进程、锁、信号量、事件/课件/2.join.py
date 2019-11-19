# print(__name__)
# print(type(__name__))

#(1)
# import mymodule
# print(mymodule.a)

#(2)
# from mymodule import a
# print(a)

#(3) __name__
''' 
如果作为一个主文件执行,得到的时__main__
如果作为一个分模块导入,那么返回的时模块名称;
是主进程,返回__main__ 不是主进程,返回模块名;
'''



# ### join 等待有子进程执行完毕之后,主进程在向下执行;
from multiprocessing import Process
import time
'''
# (1)join 基本用法
def func():
	print("发送第一封邮件")
	
if __name__ == "__main__":
	p = Process(target=func)
	p.start()
	# time.sleep(0.5)
	p.join()
	print("发送第二封邮件")
'''

# (2)多个子进程通过join加阻塞,可以和主进程进行同步控制
'''等我子进程全部执行完毕之后,主进程在走'''
'''
def func(index):
	print("第%s封邮件已经发送..." % (index))

if __name__ == "__main__":
	lst= []
	for i in range(10):
		p = Process(target = func ,args=(i,))
		p.start()
		lst.append(p)
		
	for i in lst:
		i.join()
	
	print("发送第十封邮件...")
'''
# ### 使用第二种方法创建进程
'''用自定义类的方式创建进程'''
'''
必须继承父类Process
里面必须用run命名方法;
'''
#(1) 基本使用
import os
'''

class MyProcess(Process):
	def run(self):
		print("1子进程id>>>:%s,父进程id>>>:%s" % (os.getpid(),os.getppid()) )

if __name__ == "__main__":
	p = MyProcess()
	p.start()
	print("主进程:{}".format(os.getpid()))
'''

#(2) 带参数的子进程函数
class MyProcess(Process):


	def __init__(self,arg):
		# 调用一下父类的构造方法来进行初始化
		super().__init__()
		self.arg = arg

	def run(self):
		print("1子进程id>>>:%s,父进程id>>>:%s" % (os.getpid(),os.getppid()) )
		print(self.arg)
		
if __name__ == "__main__":
	lst = []
	for i in range(10):
		p = MyProcess("参数:%s" % (i))
		p.start()
		lst.append(p)
		
	for i in lst:
		i.join()
		
	print("最后执行子进程这句话:",os.getpid())
		
		







