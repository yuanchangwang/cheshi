# ### 生成器 元组推导式是生成器(generator) 
'''
定义:生成器可以实现自定义,迭代器是系统内置的,不能够更改
生成器的本质就是迭代器,只不过可以自定义.

生成器有两种定义的方式:
(1) 生成器表达式  (里面是推导式,外面用圆括号)
(2) 生成器函数 
'''
# (1) 元组推导式的形式来写生成器 
gen = (i * 2 for i in range(5))
print(gen)
from collections import Iterator
print(isinstance(gen,Iterator))

# (2)使用for循环进行调用
for i in gen:
	print(i)
	
# (3)还可以使用next进行调用
gen = (i * 2 for i in range(5))
res  = next(gen)
print(res)
res  = next(gen)
print(res)
res  = next(gen)
print(res)
res  = next(gen)
print(res)
res  = next(gen)
print(res)

# res  = next(gen) # error 越界错误 next调用生成器 是单向不可逆的过程.
# print(res)

# (4) 利用for 和next 配合使用 调用生成器
gen = (i * 2 for i in range(5))
for i  in  range(3):
	res = next(gen)
	print(res)




























