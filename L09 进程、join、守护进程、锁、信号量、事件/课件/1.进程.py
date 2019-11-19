# ### 进程
import os,time
from multiprocessing import Process
'''
# 获取子进程id (当前进程)
res = os.getpid()
print(res)

# 获取父进程id
res= os.getppid()
print(res)
'''
# (1) 进程的基本语法
'''
def func():
	print("1子进程id>>>:%s,父进程id>>>:%s" % (os.getpid(),os.getppid()) )

if __name__ == "__main__":
	print("2子进程id>>>:%s,父进程id>>>:%s" % (os.getpid(),os.getppid()) )
	# 创建子进程 target 是指定要完成的任务,后面接的是函数变量
	p = Process(target=func)
	# 调用子进程
	p.start()
'''
# (2) 带有参数的函数
'''
def func():
	for i in range(1,6):
		print("1子进程id>>>:%s,父进程id>>>:%s" % (os.getpid(),os.getppid()) )

if __name__ == "__main__":
	print("2子进程id>>>:%s,父进程id>>>:%s" % (os.getpid(),os.getppid()) )
	p = Process(target=func)
	# 调用子进程
	p.start()
	
	n = 5
	for i in range(1,n+1):	
		print("*"*i)
'''

"""
def func(n):
	for i in range(1,n+1):
		time.sleep(0.3)
		print("1子进程id>>>:%s,父进程id>>>:%s" % (os.getpid(),os.getppid()) )

if __name__ == "__main__":
	print("2子进程id>>>:%s,父进程id>>>:%s" % (os.getpid(),os.getppid()) )
	'''
	# 创建子进程,返回进程对象,如果有参数用args关键字参数进行指定
	# 对应的值是元组,参数赛到元组当中,按照传递次序排列
	'''
	n = 5
	p = Process(target=func,args=(n,))
	p.start()
	
	for i in range(1,n+1):
		time.sleep(0.1)
		print("*" * i)
"""
# (3) 进程之间数据彼此隔离
"""
count = 99
def func():
	global count
	count += 1
	print("子进程id:%s" % (os.getpid()))
	print(count)
	
	
if __name__ == "__main__":
	p = Process(target=func)
	p.start()
	time.sleep(1)
	print("我是主进程,count=",count)
"""

# (4) 多进程之间的并发
# 在程序并发时,因为cpu的调度策略问题,不一定谁先执行,谁后执行,任务的执行,是资源抢占的过程
"""
def func(i):
	print("i=%s,1子进程id>>>:%s,父进程id>>>:%s" % (i,os.getpid(),os.getppid()) )


if __name__ == "__main__":
	for i in range(10):
		Process(target=func,args=(i,)).start()
"""
# (5) 子进程和父进程之间的关系
"""
通常情况下,父进程(主进程)速度执行稍块,但是不绝对
在父进程执行所有代码完毕之后,会默认等待所有子进程执行完毕
然后在彻底程序,为了方便进程的管理

如果不等待,子进程会变成僵尸程序,在后台不停的占用内存和cpu
因为进程太多,一时找不到,并不容易.
"""
def func(args):
	print("1子进程id>>>:%s,父进程id>>>:%s" % (os.getpid(),os.getppid()) )
	time.sleep(0.3)
	print("end,args= ",args)
	
if __name__ == "__main__":
	for i in range(10):
		Process(target= func,args=(i,)).start()
		
	print("主进程执行结束....")
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
