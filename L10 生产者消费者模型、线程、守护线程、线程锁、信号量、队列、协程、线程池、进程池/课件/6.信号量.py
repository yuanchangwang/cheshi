# ### 信号量 (线程)
from threading import Semaphore,Thread
import time,random

def func(i,sem):
	time.sleep(random.uniform(0.1,1))
	"""
	with 锁: 自动完成上锁和解锁操作
	"""
	with sem:
		print(i)
		time.sleep(random.uniform(3,6))


if __name__ == "__main__":
	
	sem = Semaphore(5)
	for i in range(20):
		Thread(target = func,args=(i,sem)).start()












































