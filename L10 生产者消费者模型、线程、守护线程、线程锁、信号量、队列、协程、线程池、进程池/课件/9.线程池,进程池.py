# ### 新版进程池,线程池
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import os,time

# (1) 进程池 允许cpu并行
def func(i):
	print("Process:",i,os.getpid())
	time.sleep(3)
	print("Process: end")
	return 5488
"""
if  __name__ == "__main__":
	# 1.创建进程池对象
	'''
	如果使用了进程池,是要控制进程并行数量的,
	6是代表最大6个进程
	ProcessPoolExecutor 后面的参数默认是cpu的最大逻辑处理器核心数.
	'''
	p = ProcessPoolExecutor()
	# 2.异步触发进程
	# res 接收的是对象,这个对象可以通过result()来获取返回值
	res = p.submit(func,1)
	print(res,type(res))
	
	
	# for i in range(10):
		# res = p.submit(func,i)
	
	
	# 3.获取进程任务的返回值
	res2 = res.result()
	print(res2) #5488
	# 4.shutdown,等待所有子进程执行完毕之后,在向下执行,类似于join
	p.shutdown()
	print("主进程执行完毕")
"""

# (2) 线程池
"""
GIL锁:一个进程中的多条线程同一时间只能被一个cpu执行,不能实现并行操作.
想要解决:更换Jpython 或者 PyPy解释器
为什么加锁:
	python是解释性语言,编译一行,就执行一行,不能提前规划系统资源,进行全局分配,根本原因是历史遗留问题.
	
加锁影响使用么?
	程序分为两大类:
	(1)计算密集型程序
		通过c语言改写python部分模块来实现
	(2)io密集型程序
		类似于python_web 运维,数据分析 都可以使用,绰绰有余.

"""
"""
from threading import current_thread as cthread
def func(i):
	print("thread",i,cthread().ident)
	time.sleep(3)
	print("thread %s end" % (i))

# 创建线程池 ,括号里可以指定并发的线程数
tp = ThreadPoolExecutor(4)
for i in range(20):
	tp.submit(func,i)
tp.shutdown()
print("主线程执行结束...")
"""

# (3) 线程池的返回值
'''
from threading import current_thread as cthread
def func(i):
	print("thread",i,cthread().ident)
	time.sleep(0.9)
	return cthread().ident
	
tp = ThreadPoolExecutor(5)
lst = []
setvar = set()
for  i  in range(10):
	res = tp.submit(func,i)
	lst.append(res)

for i in lst:
	#获取该线程对象的返回值.
	# print(i.result())
	# 把所有的线程号拿出来放到集合当中,自动去重,以验证线程池最多并发5个任务.
	setvar.add(i.result())
	

print(setvar)
print("主线程执行结束")
'''
# (4) map 返回迭代器
from threading import current_thread as cthread
def func(i):
	time.sleep(0.2)
	print("thread",i,cthread().ident)
	print("thread .. end %s" % (i))
	return "*" * i
	
tp = ThreadPoolExecutor(5)
it = tp.map(func,range(20))
tp.shutdown()
print("<===>")
from collections import Iterator
res = isinstance(it,Iterator)
print(res)
print(list(it))

# "1234567"
# it = map(int,"1234567")
# print(list(it))






