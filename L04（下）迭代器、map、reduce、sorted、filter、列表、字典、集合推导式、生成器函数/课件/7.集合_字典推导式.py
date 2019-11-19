# ### 集合推导式
"""
案例:
	满足年龄在18到21,存款大于等于5000 小于等于5500的人,
	开卡格式为:尊贵VIP卡老x(姓氏),否则开卡格式为:抠脚大汉卡老x(姓氏)	
	把开卡的种类统计出来
"""
listvar = [
	{"name":"王家辉","age":18,"money":10000},
	{"name":"王水机","age":19,"money":5100},
	{"name":"王鹏","age":20,"money":4800},
	{"name":"李站","age":21,"money":2000},
	{"name":"李小龙","age":180,"money":20}
]
'''
setvar = {} 代表字典
()    代表空元祖
(1)   代表整型1
(1,)  代表元组
set() 代表空集合
'''
setvar = set()
print(type(setvar))
# (1) (1,) ("dfdf") {} 
for i in listvar :
	if 5000 <=i['money'] <= 5500 and 18 <= i['age'] <= 21:
		setvar.add("尊贵vip老"+i['name'][0])
	else:
		setvar.add("抠脚大汉卡老"+i['name'][0])
print(setvar)
#  三目运算符   +   推导式
# 三目运算符
# "尊贵vip老"+i['name'][0] if  5000 <= i['money']<=5500 and 18 <= i['age']<=21  else  "抠脚大汉卡老"+i['name'][0]
# 推导式
# for i in listvar
setvar = {"尊贵vip老"+i['name'][0] if  5000 <= i['money']<=5500 and 18 <= i['age']<=21  else  "抠脚大汉卡老"+i['name'][0]    for i in listvar }
print(setvar)


# ### 字典推导式

### (1)enumerate
'''
enumerate(iterable,[start=0])
功能:枚举 ; 将索引号和iterable中的值,一个一个拿出来配对组成元组放入迭代器中
参数:
    iterable: 可迭代性数据 (常用:迭代器,容器类型数据,可迭代对象range) 
    start:  可以选择开始的索引号(默认从0开始索引)
返回值:迭代器
'''
listvar = ["a","b","c","d"]
res = enumerate(listvar)
print(res)
# Iterator 迭代器 Iterable 可迭代对象
from collections import Iterator,Iterable
print(isinstance(res,Iterator))
print(list(res))

# 特别指定开始值是14 不是默认0
res = enumerate(listvar,start=14)
print(list(res))

# lst = [(14, 'a'), (15, 'b'), (16, 'c'), (17, 'd')]
# res = dict(lst)
# print(res)

# 用enumerate 实现字典推导式
dictvar = {a:b for a,b in enumerate(listvar,start=7)}
print(dictvar)

# 用dict进行强转 (强转enumerate返回的迭代器)
res = dict(enumerate(listvar,start=8))
print(res)
'''
相当于
# lst = [(14, 'a'), (15, 'b'), (16, 'c'), (17, 'd')]
# res = dict(lst)
'''

### (2)zip
'''
zip(iterable, ... ...)
    功能: 将多个iterable中的值,一个一个拿出来配对组成元组放入迭代器中
    iterable: 可迭代性数据 (常用:迭代器,容器类型数据,可迭代对象range) 
返回: 迭代器

# 注意:2个值得索引号需要相同,如果有余出的自动舍弃.
'''
list1 = ["a","b","c","d"]
list2 = [1,2,3,4,5,6,7,8,8,9,99,0,0]
it = zip(list1,list2)
print(isinstance(it,Iterator))
print(list(it))
#返回值 [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

# 利用zip实现字典推导式
dic = { k:v for k,v in zip(list1,list2) }
print(dic)

# 利用dict 强转zip迭代器变成字典
res = dict(zip(list1,list2))
print(res)
























