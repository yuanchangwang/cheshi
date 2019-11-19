"""
# 爬虫例子:
1号进程负责爬取网页中所有内容
2号进程负责匹配提取网页中的关键字

1号进程就可以看成一个生产者
2号进程就可以看成一个消费者

有时可能生产者必消费者块,反之亦然
所以为了减少生产者和消费者速度上的差异化,加了一个中间的缓冲队列

生茶这和消费者模型从程序上看就是一个存放数据和拿取数据的过程
最为理想的生产者消费者模型,两者之间的速度相对平均.
"""
from multiprocessing import Process,Queue
import random,time

# 消费者模型(负责取值)
def consumer(q,name):
	while True:
		food = q.get()
		if food is None:
			break
		time.sleep(random.uniform(0.1,1))
		print("%s 吃了一个%s" % (name,food))
	
# 生产者模型(负责存值)
def producer(q,name,food):
	for i in range(3):
		time.sleep(random.uniform(0.1,1))
		print("%s 生产了 %s,%s" % (name,food,i))
		q.put(food + str(i))


if __name__ == "__main__":
	q = Queue()
	# 1号消费者
	c1 = Process(target=consumer,args=(q,"徐欣欣"))
	c1.start()
	
	# 1号生产者
	p1 = Process(target=producer,args=(q,"龙阳","土豆"))
	p1.start()
	
	p1.join()
	q.put(None)







































