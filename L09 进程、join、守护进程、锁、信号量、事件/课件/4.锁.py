# ### 锁
from multiprocessing import Lock,Process
import json,time
"""
语法:
# 创建一把锁
lock = lock()
# 上锁
lock.acquire()
# 解锁
lock.release()
"""

# 死锁  上锁和解锁之间不匹配,只上锁不解锁就是死锁,会产生阻塞;
lock = Lock()
# lock.acquire()
# lock.acquire()
# lock.release()
# lock.release()
# print(111)


# 读取票数,更新票数
def wr_info(sign,dic=None):
	if sign == "r":
		with open("ticket",mode="r",encoding="utf-8") as fp:
			dic = json.load(fp)
		return dic
		
	elif sign == "w":
		with open("ticket",mode="w",encoding="utf-8") as fp:
			json.dump(dic,fp)

# 抢票方法
def get_ticket(person):
	dic = wr_info("r")
	time.sleep(0.11)
	if dic["count"] > 0:
		print("%s抢到票了" % (person))
		dic["count"] -= 1
		# 更新数据库
		wr_info("w",dic)
	else:
		print("%s没有买到这个票" % (person))

# 用ticket来进行统一调用
def ticket(person,lock):
	# 查询票数
	dic = wr_info("r")
	print("%s 查询余票: %s" % (person,dic['count']))
	
	lock.acquire()
	# 开始抢票
	get_ticket(person)
	lock.release()


if __name__ == "__main__":
	lock = Lock()
	for i in range(10):
		p = Process(target = ticket,args=(   "person%s" % (i)  ,  lock )  )
		p.start()


# (2) 区分同步和一步
# 在产生进程对象的时候,进程之间是异步的.上锁之后,进程是同步的
# 必须等上一个进程执行完毕之后,下一个进行才能执行,这个是同步.






