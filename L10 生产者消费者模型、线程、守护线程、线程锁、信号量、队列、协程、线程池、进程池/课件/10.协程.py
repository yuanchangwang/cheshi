# ### 协程
'''
def gen():
	for i in range(10):
		yield i

# 初始化生成器函数 返回生成器对象,简称生成器
mygen = gen()
# for i in mygen:
	# print(i)

for i in range(3):
	res = next(mygen)
	print(res)

# (1) 用协程改写生产者消费者模型
def producer():
	for i in range(100):
		yield i 
		
def consumer():
	g = producer()
	for i in g:
		print(i)

consumer()
'''
# (2) 协程的具体实现
'''
switch 一般遇到阻塞时,可以手动调用该函数进行任务切换
缺点:不能够自动规避io,即不能自动实现遇到阻塞就切换
'''

import time
"""
from greenlet import greenlet
def eat():
	print("eat one")
	g2.switch()
	time.sleep(1)
	print("eat two")

def play():
	print("play one")
	time.sleep(1)
	print("play two")
	g1.switch()

g1 = greenlet(eat)
g2 = greenlet(play)
g1.switch()
"""

# (3) gevent  缺陷:不能够识别time.sleep 阻塞
import gevent
"""
spawn 类似于switch 自动进行任务切换
"""
'''
def eat():
	print("eat one")
	time.sleep(1)
	print("eat two")

def play():
	print("play one")
	time.sleep(1)
	print("play two")

	
# 利用gevent 创建协程对象g1
g1 = gevent.spawn(eat)
# 利用gevent 创建协程对象g2
g2 = gevent.spawn(play)

g1.join() #阻塞,直到g1协程任务执行完毕
g2.join() #阻塞,直到g2协程任务执行完毕
print("主线程执行完毕")
'''
# (4) 进阶改造 用gevent.sleep 取代 time.sleep()
# 自动实现任务切换
'''
def eat():
	print("eat one")
	gevent.sleep(1)
	print("eat two")

def play():
	print("play one")
	gevent.sleep(1)
	print("play two")
# 利用gevent 创建协程对象g1
g1 = gevent.spawn(eat)
# 利用gevent 创建协程对象g2
g2 = gevent.spawn(play)

g1.join()
g2.join()

print("主线程执行结束")
'''
# (5) 终极解决不识别问题
from gevent import monkey
# ba patch_all 下面所有引入的模块所包含的阻塞,重新识别出来.
monkey.patch_all()
import time
import gevent
def eat():
	print("eat one")
	time.sleep(1)
	print("eat two")

def play():
	print("play one")
	time.sleep(1)
	print("play two")

g1 = gevent.spawn(eat)

g2 = gevent.spawn(play)

g1.join()
g2.join()
print("主线程执行结束")


























