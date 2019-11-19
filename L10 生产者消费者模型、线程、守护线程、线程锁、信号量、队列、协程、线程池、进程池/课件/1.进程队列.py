# ### 进程队列
from multiprocessing import Process,Queue

# (1) 基本语法
'''先进先出,后进后出'''
"""
q = Queue()
# 1.把数据放到q队列中 put
q.put(111)
# 2.把书局从队列中拿出来 get
res = q.get()
print(res)
"""
# 3.当队列里面的值都拿出来了,已经没有数据的时候,在获取会阻塞
# res = q.get()
# 4.get_nowait 无论有没有都拿,如果拿不到,直接报错
# res = q.get_nowait()

# 异常处理 ： 抑制错误
"""
try:
	code1
	code2
except:
	code1
	code2
把可能出现异常的代码扔到try代码块中
如果发生异常,直接执行except中的代码块,抑制错误	
"""
# res = q.get_nowait()
"""
try:
	res = q.get_nowait()
except:
	pass
"""

# (2)  可以使用queue 指定队列长度
"""最多放3个,超过最大长度再放,直接阻塞"""
"""
q = Queue(3)
q.put(1)
q.put(2)
q.put(3)
# q.put(4) 阻塞 如果队列已经满了,在放值,直接阻塞

# put_nowait 如果队列已经满了,再放值,直接报错
try:
	q.put_nowait(4)
except:
	pass
"""
# (了解 full empty 不常用 )
# 如果队列满了,返回真,反之亦然
	# res = q.full()
	# print(res)
	# q.get()
# q.get()
# q.get()
# 如果队列空了,返回真,反之亦然
# print(q.empty())


# (3) 进程之间的通讯
def func(q1):
	# 1.主进程添加的值,子进程可以通过队列拿到
	res = q1.get()
	print("我是子进程",res)
	q1.put(2233)


if __name__ == "__main__":
	print("<======================>")
	q1 = Queue()
	p = Process(target=func,args=(q1,))
	p.start()
	
	# 主进程添加数据
	q1.put("aaabbb")
	p.join()
	# 2.子进程添加的值,主进程通过队列拿到
	res = q1.get()
	print(res)
	
	




























