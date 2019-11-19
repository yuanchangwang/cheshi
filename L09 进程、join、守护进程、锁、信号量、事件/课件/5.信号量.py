# ### 信号量 Semaphore 本质上就是锁,只不过可以控制锁的数量
from multiprocessing import Process,Semaphore
import random,time,os

def ktv(person,sem):
	time.sleep(0.1)
	sem.acquire()	
	print("%s进入ktv开始唱歌" % (person))
	print(os.getpid())
	time.sleep(3)	
	print("%s走出ktv离开" % (person))
	sem.release()


if __name__ == "__main__":
	sem = Semaphore(4)
	for i in range(10):
		p = Process(target=ktv,args=("person%s" %(i),sem) )
		p.start()





