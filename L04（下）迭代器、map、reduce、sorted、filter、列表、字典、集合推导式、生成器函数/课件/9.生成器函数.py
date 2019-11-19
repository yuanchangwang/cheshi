# ### yield  生成器函数
'''
# yield 类似于 return
共同点在于:执行到这句话都会把值返回出去
不同点在于:yield每次返回时,会记住上次离开时执行的位置 , 下次在调用生成器 , 会从上次执行的位置往下走
		   而return直接终止函数,每次重头调用.
yield 6 和 yield(6) 2种写法都可以 yield 6 更像 return 6 的写法 推荐使用
'''
# (1) 定义一个生成器
def func():
	print("one")
	yield  1
	
	print("two")
	yield 2
	
	print("three")
	yield 3
	
# 初始化生成器函数 => 返回一个生成器对象 简称生成器
gen = func()

res = next(gen)
print(res)
res = next(gen)
print(res)
res = next(gen)
print(res)
# res = next(gen) # error
# print(res)

'''
# 代码解析;
	首先初始化生成器函数 返回生成器对象,简称生成器
	有了生成器之后 可以使用next进行依次的调用
	第一次 print(one)   记录当前的状态,暂停等待下一次调用 通过yield 1 返回1 ,阻塞代码在第11行
	第二次 print(two)   记录当前的状态,暂停等待下一次调用 通过yield 2 返回2 ,阻塞代码在第14行
	第三次 print(three) 记录当前的状态,暂停等待下一次调用 通过yield 3 返回3 ,阻塞代码在第17行
	到此已经没有值可以在拿出来了,如果在调用,直接越界报错.
'''

# (2) 优化生成器
def func():
	for i in range(1,101):
		yield "我的球衣号码是%d" % (i)

# 初始化生成器函数 => 返回一个生成器对象
gen = func()

for i  in  range(30):	
	res = next(gen)
	print(res)
	
for i in range(50):
	res = next(gen)
	print(res)

# (3)  send  把值发送给上一个yield 进行接收
### send
'''
# next和send区别:
	next 只能取值
	send 不但能取值,还能发送值
# send注意点:
	第一个 send 不能给 yield 传值 默认只能写None (语法的硬性要求)
	最后一个yield 接受不到send的发送值
'''

def func():
	print("start")
	res = yield 1
	print(res)

	res = yield 2
	print(res)
	
	res = yield 3
	
	
	
	print(res)	
	print("end")

# 第一步:初始化生成器函数 => 生成器对象 简称生成器
gen = func()
# 生成器.send  第一次发送的时候必须参数是None 硬性语法
res = gen.send(None)
print(res)
# res = next(gen)
# print(res)
# 第二次可以自定义要发送的值 
res = gen.send("111")
print(res)

res = gen.send("222")
print(res)

"""如果没有yield了 , 就没有返回值给你, 在调用直接报错."""
"""如果就像在最后一次调用的时候执行剩下的没跑完的代码,使用try..except..来进行异常处理"""
# res = gen.send("333") #  会出现越界错误StopIteration
# print(res)

"""
发送的时候 是先发送 ,后接受

#第一次发送的时候必须参数是None 硬性语法
print(start) 记录当前状态, 把yield 1这个值返回取出 , 暂定阻塞,等待下一次调用.
# 第二次调用时,可以自定义要发送的值 被yield 1 这一行收走了,res接收到send发送过去的值为111
那么从这一行继续向下执行
print(res) 111
res = yield 2
把2 返回给res = gen.send(111) 这一行 res 接收到2 print(res)

#第三次调用时,发送自定义值222,被res = yield 2接收到 print(res) => 222
然后执行res = yield 3 记录当前状态,把yield 3 这个值返回取出, 代码暂停阻塞,等待下一次调用.
"""

# ### yield from : 将一个可迭代对象变成一个迭代器返回	
def func():
	listvar = [1,2,3,4,4,5]
	# yield listvar
	yield from listvar
	
# 初始化生成器函数 返回生成器对象 简称生成器
print("<==>")
gen = func()
res = next(gen)
print(res)
res = next(gen)
print(res)
res = next(gen)
print(res)
res = next(gen)
print(res)
print("<==>")
for i in gen:
	print(i)




















