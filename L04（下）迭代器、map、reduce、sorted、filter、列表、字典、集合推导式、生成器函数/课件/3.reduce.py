# ### reduce
'''
reduce(func,iterable)
功能:
	计算
	首先把iterable 当中的两个值拿到func当中进行运算,计算的结果在和iterable中的第三个值
	拿到func中计算,依次类推.返回最终的结果
参数:
	func 自定义函数 或者 内置函数
	iterable 可迭代对象(常用:容器类型数据 range对象 迭代器)
返回值:
	最终的计算结果
'''

# [5,4,9,9] => 5499
'''
#1
strvar = ''
for  i in [5,4,9,9]:
	strvar += str(i)
print(strvar,type(strvar))
print(int(strvar),type(int(strvar)))
'''
'''
5*10 +4 = 54
54*10+9 = 549
549*10+9 = 5499
'''

'''
#2
lst = [5,4,9,9]
it = iter(lst)
res1 = next(it)
res2 = next(it)
total = res1 * 10 + res2
print(total)

for i in it:
	#54
	# 54 * 10 + 9 = 549
	# 549 * 10 + 9 = 5499
	total = total * 10 + i
print(total)
'''

# from .. import 从哪里... 引入 functools 模块   reduce就是这个模块中的方法
from functools import reduce
def func(x,y):
	return x*10 + y
lst = [5,4,9,9]
res = reduce(func,lst)
print(res)

'''
先把列表中5和4拿出来放到func函数中用x,和 y来接收参数
x*10+y  => 5*10+4 =54
第二次 拿54 和 9两个值扔到func当中进行运算
x*10+y  => 54 * 10 + 9 => 549
第三次 拿549 和 9 两个值扔到func当中进行运算
x*10+y => 549 * 10 + 9 => 5499
到此所有计算完毕 ,返回5499
'''

# "534" => 534 禁止使用int强转 能否完成?
strvar = "534"
def func(x,y):
	return x*10 + y

# res = reduce(func,list(strvar))
# print(res) error

def func2(n):
	dic = {'0':0,'1':1,'2':2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
	return dic[n]

it = map(func2,"534")
# print(list(it))

res = reduce(func,it)
print(res)
















