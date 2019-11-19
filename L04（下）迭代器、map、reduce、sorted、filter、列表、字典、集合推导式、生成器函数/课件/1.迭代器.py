# ### 迭代器
'''能被next进行调用,并且不断返回下一个值的对象'''
'''
特征:迭代器会生成惰性序列,它通过计算把值依次的返回,一边循环一边计算而不是一次性得到所有数据
优点:需要数据的时候,一次取一个,可以大大节省内存空间.而不是一股脑的把所有数据放进内存.
可以遍历无限量的数据
next调用迭代器时,方向是单向不可逆的.
'''
setvar = {1,2,"abc",54,"dd"}
for i in setvar:
	print(i)

# (1)可迭代性对象
'''__iter__ 如果这个数据类型含有__iter__ 方法 我们就说他是可迭代对象'''
# dir 获取当前数据内置的方法和属性.
lst = dir(setvar)
print(lst)
print("__iter__" in lst)
'''
[
'__and__', 
'__class__', 
'__contains__', 
'__delattr__', 
'__dir__', 
'__doc__', 
'__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
'__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', 
'__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__',
 '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__',
 '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', 
 '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 
 'difference_update', 'discard', 'intersection', 'intersection_update',
 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 
 'symmetric_difference_update', 'union', 'update']

'''

# (2)迭代器

'''
可迭代型数据:可以遍历的数据
for 循环在遍历集合的时候,在底层用next方法实现的集合的调用

区别:
可迭代对象 -> 迭代器  不可直接调用 -> 可直接调用的过程

如何变成迭代器?
(1) iter (2)__iter__()
如何遍历迭代器?
(1) next (2)__next__()
如何判断迭代器?
__iter__ __next__ 如果含有这两个方法,就说他是迭代器


可迭代对象不一定是迭代器
迭代器一定是可迭代对象


'''
setvar = {1,2,"abc",54,"dd"}
it = iter(setvar)
lst = dir(it)
print(lst)
print('__iter__' in lst and '__next__' in lst)
res = next(it)
print(res)
res = next(it)
print(res)
res = next(it)
print(res)
res = next(it)
print(res)
res = next(it)
print(res)

# (3) 判断是否是可迭代对象或者迭代器
# from .. import 从哪个模块  ...  引入 ...东西
# 从collections模块 引入 Iterator类型(迭代器类型) Iterable(可迭代对象)
from collections import Iterator,Iterable
# 1.判断集合的迭代属性
setvar = {1,2,"abc",54,"dd"}
res = isinstance(setvar,Iterable)
print(res)
res = isinstance(setvar,Iterator)
print(res)

# 2.判断range对象的迭代属性
print(isinstance(range(10),Iterable)) # True
print(isinstance(range(10),Iterator)) # False


it = iter(range(10))
res = next(it)
print(res)
res = next(it)
print(res)

# 3.遍历迭代器
it = iter(range(10))
for i in it:
	print(i)
# StopIteration 是迭代器的越界现象错误
# res = next(it)
# print(res)

# 4.重置迭代器
it = iter(range(10))
# for i in it:
	# print(i)
	
# 使用for 和 next 搭配来遍历迭代器
print("<===>")
for i  in range(3):
	res = next(it)
	print(res)





