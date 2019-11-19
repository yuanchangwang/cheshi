# ### sorted 
'''
sorted(iterable,reverse=False,key=函数)
功能:排序
参数:
	iterable:可迭代性数据(常用:容器类型数据,range对象,迭代器)
	reverse : 是否倒序
	默认正序reverse= False(从小到大) 如果reverse=True 代表倒序 (从大到小)
	key = 自定义函数 或者 内置函数
返回值:
	排序的序列
'''
listvar = [1,2,-88,-4,5]
# 按照从小到大默认排序
res = sorted(listvar)
print(res)

# 从大到小排序
res = sorted(listvar,reverse=True)
print(res)


# 按照绝对值排序 (内置函数abs)
'''
abs 绝对值函数
'''
res = abs(-1.5)
print(res)
listvar = [1,2,-88,-4,5]
res = sorted(listvar,key=abs)
print(res)
'''
abs(1) => 1
abs(2) => 2
abs(-4) => 4
abs(5) => 5
abs(-88) => 88
'''

# 按照余数排序 (自定义函数)
listvar = [19,23,44,57]
def func(n):
	return n % 10 
	
res = sorted(listvar,key=func)
print(res)
'''
23 => 3
44 => 4
57 => 7
19 => 9
'''
listvar = [4,1,2,9]
listvar.sort()
print(listvar)
'''
# sort 基于原有列表进行修改
# sorted 是产生一个新列表
除此之外,所有用法全都相同
'''























