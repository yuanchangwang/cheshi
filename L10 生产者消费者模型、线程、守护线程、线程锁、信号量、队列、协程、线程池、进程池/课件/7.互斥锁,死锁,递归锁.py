# ### 死锁,递归锁,互斥锁
from threading import Thread,Lock
import time
'''
noodle = Lock()
kuaizi = Lock()
def eat1(name):
	noodle.acquire()
	print("%s拿到面条" % (name))
	kuaizi.acquire()
	print("%s拿到筷子" % (name))
	
	print("吃一会")
	time.sleep(0.5)
	
	kuaizi.release()
	print("%s放下筷子" % (name))
	noodle.release()
	print("%s放下面条" % (name))

def eat2(name):
	kuaizi.acquire()
	print("%s拿到筷子" % (name))
	noodle.acquire()
	print("%s拿到面条" % (name))

	print("吃一会")
	time.sleep(0.5)
	
	noodle.release()
	print("%s放下面条" % (name))
	kuaizi.release()
	print("%s放下筷子" % (name))


if __name__ == "__main__":
	name_lst1 = ['徐欣欣',"龙阳"]
	name_lst2 = ['周瑾',"全还一"]
	for name in name_lst1:
		Thread(target=eat1,args=(name,)).start()
		
	for name in name_lst2:
		Thread(target=eat2,args=(name,)).start()
'''

# ### (2) 递归锁
"""
递归锁,上几把锁,就解几把锁
"""
from threading import Thread,RLock
rlock = RLock()
def func(name):
	rlock.acquire()
	print(name,1)
	rlock.acquire()
	print(name,2)
	rlock.acquire()
	print(name,3)
	rlock.release()
	rlock.release()
	rlock.release()

for i in range(10):
	t = Thread(target=func,args=("name%s" % (i),) )
	t.start()
	
print("程序执行结束")
	

# ### (3) 利用递归锁,解决死锁现象
"""
	递归锁专门用于解决死锁现象,
	临时用于快速解决服务器崩溃死锁的问题,用递归锁应急问题
"""
# noodle = Lock()
# kuaizi = Lock()
'''
noodle = kuaizi =RLock()
def eat1(name):
	noodle.acquire()
	print("%s拿到面条" % (name))
	kuaizi.acquire()
	print("%s拿到筷子" % (name))
	
	print("吃一会")
	time.sleep(0.5)
	
	kuaizi.release()
	print("%s放下筷子" % (name))
	noodle.release()
	print("%s放下面条" % (name))

def eat2(name):
	kuaizi.acquire()
	print("%s拿到筷子" % (name))
	noodle.acquire()
	print("%s拿到面条" % (name))

	print("吃一会")
	time.sleep(0.5)
	
	noodle.release()
	print("%s放下面条" % (name))
	kuaizi.release()
	print("%s放下筷子" % (name))


if __name__ == "__main__":
	name_lst1 = ['徐欣欣',"龙阳"]
	name_lst2 = ['周瑾',"全还一"]
	for name in name_lst1:
		Thread(target=eat1,args=(name,)).start()
		
	for name in name_lst2:
		Thread(target=eat2,args=(name,)).start()
'''

# ### (4) 互斥锁
"""
	从语法上来看,锁是可以互相嵌套的,但是不要使用
	上一次锁,就对应解开一把锁,形成互斥锁
	吃面条和拿筷子是同时的,上一把锁就够了,不要分开上锁
	也不要去写锁的嵌套,容易死锁
"""
print("<================>")
mylock = Lock()
def eat1(name):
	mylock.acquire()
	print("%s拿到面条" % (name))

	print("%s拿到筷子" % (name))
	
	print("吃一会")
	time.sleep(0.5)
	

	print("%s放下筷子" % (name))
	print("%s放下面条" % (name))
	mylock.release()
	

def eat2(name):
	mylock.acquire()
	print("%s拿到筷子" % (name))

	print("%s拿到面条" % (name))

	print("吃一会")
	time.sleep(0.5)	

	print("%s放下面条" % (name))
	print("%s放下筷子" % (name))
	mylock.release()



if __name__ == "__main__":
	name_lst1 = ['徐欣欣',"龙阳"]
	name_lst2 = ['周瑾',"全还一"]
	for name in name_lst1:
		Thread(target=eat1,args=(name,)).start()
		
	for name in name_lst2:
		Thread(target=eat2,args=(name,)).start()



















