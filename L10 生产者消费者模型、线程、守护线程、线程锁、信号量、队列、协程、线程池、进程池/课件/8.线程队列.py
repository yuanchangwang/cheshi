# ### 线程队列
from queue import Queue
"""
put 往线程队列里防止,超过队列长度,直接阻塞
get 从队列中取值,如果获取不到,直接阻塞
put_nowait: 如果放入的值超过队列长度,直接报错
get_nowait: 如果获取的值已经没有了,直接报错
"""

# (1) queue 先进先出
q = Queue()
q.put(11)
q.put(22)
print(q.get())
print(q.get_nowait())
# print(q.get_nowait())# 直接报错

# 指定队列长度
q2 = Queue(2)
q2.put(33)
q2.put(44)
# q2.put(55)
# q2.put_nowait()

# (2) LifoQueue 后进先出 (数据结构中,栈队列的一种储存顺序)
from queue import LifoQueue
lq = LifoQueue()
lq.put(55)
lq.put(66)
print(lq.get())
print(lq.get())

# (3) PriorityQueue 按照优先级顺序排列
from queue import PriorityQueue
"""
默认按照数字大小排序,然后会按照ascii编码在从小到大排序
先写先排,后写后排
"""
pq = PriorityQueue()
pq.put( (12,"zhangsan") )
pq.put( (6,"lisi") )
pq.put( (19,"wangwen") )
pq.put( (19,"wangwen") )


# pq.put( ("zhangsan",3,99) )
# pq.put( ("lisi",12,99) )


print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())

# 单独一个元素,必须放同一种类型
# 数字类型
pg = PriorityQueue()
pg.put(13)
pg.put(18)
pg.put(3)
# pg.put("sdfsdf") 不支持
print(pg.get())
print(pg.get())
print(pg.get())


# 字符串类型
pg1 = PriorityQueue()
pg1.put("ab")
pg1.put("cc")
print(pg1.get())
print(pg1.get())

















