# ### 线程的数据安全 Lock
"""
用上锁的方式,来保证数据的安全,会牺牲一点速度.
"""
from threading import Thread,Lock
n = 0
lst = []

def func1(lock):
	global n
	for i in range(1000000):
		# 上锁修改数据
		lock.acquire()
		n-=1
		# 解锁释放
		lock.release()
		

def func2(lock):
	global n
	for i in range(1000000):
		"""
		with 语法 自动实现上锁和解锁;
		"""
		with lock:
			n+=1


if __name__ == "__main__":
	# 创建一把锁
	lock = Lock()
	for i in range(10):
		t1 = Thread(target = func1,args=(lock,))
		t2 = Thread(target = func2,args=(lock,))

		t1.start()
		t2.start()
		
		lst.append(t1)
		lst.append(t2)
		
	for i in lst:
		i.join()
		
	print("主线程执行结束:")
	print(n)

























