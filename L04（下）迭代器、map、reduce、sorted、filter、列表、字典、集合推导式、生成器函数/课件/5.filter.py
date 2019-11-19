# ### filter
'''
filter(func,iterable)
功能:过滤数据
	 如果函数的返回值是True ,代表保留当前数据
	 如果函数逇返回值是False,代表舍弃当前数据
参数:
	func 自定义函数
	iterable 可迭代对象(常用:容器类型数据,range对象,迭代器)
返回值
	迭代器
'''

listvar = [1,2,3,4,4,56,6,6,7,8,9,10]
# 要所有的偶数,舍弃所有的奇数
def func(n):
	if n % 2 == 0:
		return True
	else:
		return False
	
	
it = filter(func,listvar)
res = list(it)
print(res)


# 使用匿名函数进行优化
it = filter(lambda n :True  if n % 2 == 0 else False,listvar)
print(list(it))



