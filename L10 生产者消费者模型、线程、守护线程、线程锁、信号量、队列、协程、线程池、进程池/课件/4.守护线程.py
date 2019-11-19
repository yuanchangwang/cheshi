# ### 守护线程: 等待所有线程执行结束之后,在自动结束,守护所有线程
from threading import Thread
import time


def func1():
	while True:
		print("我是线程1,func1")


def func2():
	print("我是线程2,start")
	time.sleep(3)
	print("我是线程2,end")

# 启动线程1
t1 = Thread(target=func1)

# 守护线程语法:使用线程.setDaemon(True)
t1.setDaemon(True)
t1.start()

# 启动线程2
t2 = Thread(target=func2)
t2.start()

print("主线程执行结束")
















