# ### 线程
enumerate
from threading import Thread
from multiprocessing import Process
import random,time,os

# (1) 一个进程可以有多个线程,共享同一份资源
'''
def func(num):
	time.sleep(random.uniform(0.1,1))
	print("子线程",num,os.getpid())
	
if __name__ == "__main__":
	for i in range(10):
		t = Thread(target=func,args=(i,))
		t.start()
'''
# (2)并发多线程 和 并发多进程 的速度对比? 多线程更快
'''
def func(i):
	# time.sleep(random.uniform(0.1,1))
	print("子线程",i,os.getpid())
	
if __name__ == "__main__":
	# starttime = time.time()
	# endtime = time.time()
	# 1.计算多线程的时间
	startime = time.perf_counter()
	lst = []
	for i in range(1000):
		t = Thread(target=func,args=(i,))
		t.start()
		lst.append(t)
	
	for i in lst:
		i.join()
	
	endtime = time.perf_counter()
	print(endtime-startime,"主线程执行结束===================")

	

	# 2.计算多进程的时间
	startime = time.perf_counter()
	lst = []
	for i in range(1000):
		p = Process(target=func,args=(i,))
		p.start()
		lst.append(p)
		
	for i in lst:
		i.join()

	endtime = time.perf_counter()
	print(endtime-startime,"主进程执行结束======================")
'''

# (3)多线程共享同一份进程资源
num = 100
lst = []
def func(i):
	global num
	num -= 1
	
for i in range(100):
	t = Thread(target=func,args= (i,))
	t.start()
	lst.append(t)
	
for i in lst:
	i.join()

print(num)
	
# (4) 线程相关函数
"""
线程.is_alive()    检测线程是否仍然存在
线程.setName()     设置线程名字
线程.getName()     获取线程名字
1.currentThread().ident 查看线程id号 
2.enumerate()        返回目前正在运行的线程列表
3.activeCount()      返回目前正在运行的线程数量
"""
def func():
	# time.sleep(0.1)
	pass
	
t = Thread(target=func)
t.start()
print(t.is_alive())

t.setName("消费者-王文")
res = t.getName()
print(res)

# 1.currentThread().ident 查看线程id号 
'''
from threading import currentThread
def func():
	print("子线程:",currentThread().ident)
t = Thread(target=func)
t.start()
print("主线程:",currentThread().ident,os.getpid())
'''
# 2.enumerate()        返回目前正在运行的线程列表
'''
from threading import enumerate
def func():
	print("子线程",currentThread().ident)
	time.sleep(0.5)
	
for i in range(10):
	t = Thread(target=func)
	t.start()
print(enumerate())
print(len(enumerate()))
'''
"""
[
<_MainThread(MainThread, started 17296)>, 
<Thread(Thread-103, started 18184)>, 
<Thread(Thread-104, started 6532)>, 
<Thread(Thread-105, started 7752)>,
 <Thread(Thread-106, started 18404)>,
 <Thread(Thread-107, started 3856)>, 
 <Thread(Thread-108, started 8668)>, 
 <Thread(Thread-109, started 15612)>, 
 <Thread(Thread-110, started 15080)>, 
 <Thread(Thread-111, started 15464)>, 
 <Thread(Thread-112, started 11816)>
 ]
"""

# 3.activeCount()      返回目前正在运行的线程数量
from threading import activeCount
from threading import currentThread
def func():
	print("子线程",currentThread().ident)
	time.sleep(0.5)

for i in range(10):
	Thread(target=func).start()
print(activeCount())














