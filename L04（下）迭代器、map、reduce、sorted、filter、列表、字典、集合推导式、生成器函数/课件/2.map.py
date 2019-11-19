# ### 高阶函数 : 能够把函数当成参数传递的就是高阶函数 (map reduce sorted filter)

# map(func,iterable)
'''
功能:把iterable里面的数据一个一个的拿出来,扔到func当中进行处理,然后把处理之后的结果放到迭代器当中,最终返回迭代器
参数:
	func:自定义函数 或者 内置函数
	iterable:可迭代对象(常用:容器类型数据,range对象,迭代器)
返回值:
	迭代器
'''

# ["1","2","3","4"] => [1,2,3,4]
listvar =  ["1","2","3","4"]
'''
lst = []
for i in listvar:
	print(i,type(i))
	res = int(i)
	lst.append(res)
print(lst)
'''
from collections import Iterator,Iterable
it = map(int,listvar)
'''
每次从listvar当中拿出一个值 , 
放到int函数当中进行强转,处理后的结果扔到迭代器当中
依次类推,直到所有数据拿完为止.
'''
print(isinstance(it,Iterator))
print(isinstance(it,Iterable))
#(1)next
# res = next(it)
# print(res)
# res = next(it)
# print(res)
# res = next(it)
# print(res)
# res = next(it)
# print(res)

#(2)for
# for i in it:
	# print(i)

#(3)list 类型强转 使用list强转迭代器可以瞬间拿到迭代器中所有数据
lst = list(it)
print(lst)

# (2)[1,2,3,4] => [2,4,6,8]
# lst = []
# for i in [1,2,3,4]:
	# res = i * 2
	# lst.append(res)
# print(lst)

# 如果使用自定义方法,切记要加上return 返回值
lst = [1,2,3,4]
print("<===>")
def func(n):
	return n * 2
it = map(func,lst)
print(isinstance(it,Iterator))
print(list(it))

# (3){97:'a',98:'b',99:'c'}   ['a','b','c'] => [97,98,99]
'''
dic = {'a':97,'b':98,'c':99}
dic['a'] => 97
dic['b'] => 98
dic['c'] => 99
'''
'''
dic = {97:'a',98:'b',99:'c'}
dic2 = {}
for a,b in dic.items():
	dic2[b] = a
print(dic2)
'''
# {'a': 97, 'b': 98, 'c': 99}
lst = ['a','b','c']
def func(n):
	dic = {97:'a',98:'b',99:'c'}
	dic2 = {}
	for a,b in dic.items():
		dic2[b] = a
	return dic2[n]
	
it = map(func,lst)
print(list(it))


















