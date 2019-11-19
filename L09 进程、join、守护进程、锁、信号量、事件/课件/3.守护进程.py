# ### 守护进程
from multiprocessing import Process
import time
'''
正常情况下,主进程默认等待子进程调用结束之后结束
守护进程在主进程执行代码结束后,自动终止

守护进程语法:
进程对象.daemon = True 
设置该进程是守护进程
守护进程需要在start()方法之前设置

为主进程守护,主进程如果代码执行结束了,该守护进程自动结束.
'''

# (1) 基本语法
'''
def func():
	print("子进程start")	
	time.sleep(2)
	print("子进程end")
	
if __name__ == "__main__":
	p = Process(target=func)
	p.daemon = True
	p.start()
	print("主进程执行结束")
'''
	
# (2) 多个子进程情况
'''
当多个子进程并发执行时,默认主进程等待子进程的
如果标记该子进程是守护进程
当主进程执行完所有代码之后,守护进程立刻终止
主进程代码执行到最后一行,就意味着守护进程终止了
其他非守护进程继续执行,主进程仍然会等待他执行结束
最后主进程在真正的释放结束.
'''


'''
def func1():
	count =1
	while True:	
		print("*" * count)
		time.sleep(0.5)
		count += 1
		
def func2():
	print("func2 start")
	time.sleep(3)
	print("func2 end")

if __name__ == "__main__":
	p1 = Process(target = func1)
	p1.daemon = True;
	p1.start()
	
	p2 = Process(target = func2)
	p2.start()
	
	print("主进程代码执行完毕")
'''


# (3) 守护进程的实际用途: 报活

def alive():
	while True:
		print("1号服务主机... i am ok")
		time.sleep(0.5)
		
def func():
	print("1号服务主机负责统计日志")
	time.sleep(3)
	

if __name__ == "__main__":
	p1 = Process(target = alive)
	p1.daemon = True
	p1.start()
	
	p2 = Process(target = func)
	p2.start()
	
	# 模拟就好比这个程序结束了,或者服务器挂掉了,就停止报活
	p2.join()
	print("......")
















