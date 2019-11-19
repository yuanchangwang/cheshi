# ### 装饰器
'''
扩展函数新功能的@
定义:替换旧函数,返回新函数,在不改变原有代码的前提下,为该函数扩展新功能;
语法:@ (语法糖)
'''

# (1) 装饰器的原型
def kuozhan(func):
	def newfunc():
		print("厕所前,蓬头垢面")
		func()#print("我是个屌丝")
		print("厕所后,精神气爽")
	return newfunc
	
def func():
	print("我是个屌丝")    # func = kuozhan(func)
func = kuozhan(func)  # func = newfunc  <==> func() 就是newfunc() 一样的
print(func)

# func = kuozhan(func)
# func()

# (2) 装饰器语法@	
def kuozhan(func):
	def newfunc():
		print("厕所前,蓬头垢面")
		func()
		print("厕所后,精神气爽")
	return newfunc
@kuozhan   # func = kuozhan(func)
def func():
	print("我是个屌丝")


'''
方向:从下到上,把func当成一个参数给装饰器kuozhan,
返回的新函数覆盖旧函数func,func在调用时,相当于
调用newfunc(),只不过@自动帮助你实现了这一步,func = kuozhan(func)
直接调用即可.
'''
func()


# (3) 装饰器的嵌套
def kuozhan1(func):
	def newfunc():
		print("厕所前,蓬头垢面1")
		func()
		print("厕所后,精神气爽2")
	return newfunc

def kuozhan2(func):
	def newfunc():
		print("吃饭前,洗洗手3")
		func()
		print("吃饭后,簌簌口4")

	return newfunc


@kuozhan1
@kuozhan2
def func():
	print("我是白富美5")
 
func()
'''
# 第一步:
@kuozhan2
def func():
	print("我是白富美5")
# 结果:
def func():
	print("吃饭前,洗洗手3")
	print("我是白富美5")
	print("吃饭后,簌簌口4")

# 第二部
@kuozhan1
def func():
	print("吃饭前,洗洗手3")
	print("我是白富美5")
	print("吃饭后,簌簌口4")

# 结果:
print("厕所前,蓬头垢面1")
	# 作为一个整体调用依次
	print("吃饭前,洗洗手3")
	print("我是白富美5")
	print("吃饭后,簌簌口4")

print("厕所后,精神气爽2")

# 整体返回
'''


# (4) 带有参数的装饰器
'''# 如果原函数带有参数,  那么返回的新函数也要带有参数,(参数一一对应)'''
print("<===>")
def kuozhan(func):

	def new_func(who,where):
		print("厕所前,干净整洁")
		func(who,where)
		print("厕所后,一片狼藉")
	return new_func

@kuozhan
def func(who,where):
	print("{}在{}里解手".format(who,where))
func("豪杰","鸟窝")


print("<====>")
# (5) 带有参数返回值的装饰器
"""原函数怎么定义的参数,新函数就那样去定义"""
def kuozhan(func):
	# 函数的定义处,*args,**kwargs 是收集参数
	def new_func(*args,**kwargs):
		print("厕所前,苟延残喘")
		# * 和 ** 的魔术用法  *[1,2,3] **{'a':1,'b':2} 把容器里面的数据,一个一个拿出来当成参数赋给调用处的func
		lst = func(*args,**kwargs)
		print("厕所后,大言不惭")
		
		return lst
		
	return new_func

@kuozhan
def func(*args,**kwargs):
	# print(args)
	# print(kwargs)
	print(args)
	dictvar = {"qhy":"全海毅","hb":"胡斌","hqc":"胡启超"}
	# lst = {dictvar[a]:b  for a,b in kwargs.items() if a in dictvar}
	lst = [dictvar[a]+"生产了"+b+"便便"  for a,b in kwargs.items() if a in dictvar]
	return lst

res = func("电影院","水池",qhy="15克",hb="15斤",hqc="15顿")
print(res)













