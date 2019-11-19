# ### 事件
'''
# 阻塞事件 ：
	e = Event()生成事件对象e   
	e.wait()动态给程序加阻塞 , 程序当中是否加阻塞完全取决于该对象中的is_set() [默认返回值是False]
    # 如果是True  不加阻塞
    # 如果是False 加阻塞

# 控制这个属性的值
    # set()方法     将这个属性的值改成True
    # clear()方法   将这个属性的值改成False
    # is_set()方法  判断当前的属性是否为True  (默认上来是False)
'''
from multiprocessing import Process,Event
# (1) 基本语法:
"""
#(1)

print(e.is_set()) # 默认: False
e.wait(1)
print(123)
#(2)
e.set()
print(e.is_set()) # False
e.wait()
print(456)
"""
#(3)
"""
e = Event() # True
e.set()
e.wait()
print(123)
e.clear() # False
e.wait()
print(456)
"""
# (1)
"""
import time,random
# ### 模拟红绿灯效果 红灯停,绿灯行
def traffic_light(e):
	# 默认红灯先亮
	print("红灯亮")
	while True:
		if e.is_set():
			# 当前是绿灯等待1秒
			time.sleep(1)
			# 等完1秒后,变成红灯
			print("红灯亮")
			e.clear()
		else:
			# 当前是红灯
			time.sleep(1)
			# 等完1秒之后,变成绿灯
			print("绿灯亮")
			e.set()

# e = Event()
# traffic_light(e)

# 模拟小车遇到红灯停,绿灯行
def car(e,i):
	if not e.is_set():
		print("car%s在等待" % (i))
		e.wait()
	print("car%s通行了" % (i))


if __name__ == "__main__":
	e = Event()
	# 启动交通灯
	p1 = Process(target=traffic_light,args=(e,))
	p1.start()
	
	# 开始跑车进程
	for i in range(20):
		time.sleep(random.uniform(0,2))
		p2 = Process(target=car,args = (e,i))
		p2.start()
"""


# (2)
import time,random
# ### 模拟红绿灯效果 红灯停,绿灯行
def traffic_light(e):
	# 默认红灯先亮
	print("红灯亮")
	while True:
		if e.is_set():
			# 当前是绿灯等待1秒
			time.sleep(1)
			# 等完1秒后,变成红灯
			print("红灯亮")
			e.clear()
		else:
			# 当前是红灯
			time.sleep(1)
			# 等完1秒之后,变成绿灯
			print("绿灯亮")
			e.set()

# 模拟小车遇到红灯停,绿灯行
def car(e,i):
	if not e.is_set():
		print("car%s在等待" % (i))
		e.wait()
	print("car%s通行了" % (i))


if __name__ == "__main__":
	e = Event()
	lst = []
	# 启动交通灯
	p1 = Process(target=traffic_light,args=(e,))
	p1.daemon = True
	p1.start()
	
	# 开始跑车进程
	for i in range(20):
		time.sleep(random.uniform(0,2))
		p2 = Process(target=car,args = (e,i))
		p2.start()
		# p2.join()
		lst.append(p2)
		
	for i in lst:
		i.join()
		
	print("程序彻底结束;")
















