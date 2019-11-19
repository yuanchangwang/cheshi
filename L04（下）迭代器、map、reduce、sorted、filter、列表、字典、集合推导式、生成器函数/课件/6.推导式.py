# ### 推导式:通过一行循环判断,遍历出一系列数据的方式是推导式  (简洁方便)
'''
val for val in Iterable
'''
# 列表推导式
# [1,2,3,4] => [2,4,6,8]
"""
lst = []
for i in range(1,5):
	print(i)
	lst.append(i)
print(lst)'
"""
listvar = [i for i in range(1,5)]
print(listvar)
listvar = [i*2 for i in range(1,5)]
print(listvar)

# 带有判断条件的列表推导式
#[1,2,3,4,4,5,9,6] 只要奇数
lst = [1,2,3,4,4,5,9,6]
lst2 = []
for i  in  lst:
	if i % 2 == 1:
		lst2.append(i)
print(lst2)

res = [i for i in lst if i % 2 == 1]
print(res)

# 带有双循环的列表推导式
lst1 = ["王文","大帅哥","神秘男孩"]
lst2 = ["美女","嫩模","萝莉"]
# "" ♥♥  "" 
for i in lst1:
	for j in lst2:
		print(i,"♥♥",j)
	
res = [i+"♥♥"+j for i in lst1 for j in lst2]
print(res)


# 带有条件判断的多循环推导式
for i in lst1:
	for j in lst2:
		# 如果王文的索引号和美女的索引号相同,就把这两个值进行拼接
		if lst1.index(i) == lst2.index(j):
			print(i,"♥♥",j)
		
lst = [i+'♥♥'+j for i in lst1 for j in lst2 if lst1.index(i) == lst2.index(j) ]
print(lst)

"""
推导式的后面:只能是循环或者 判断(单项分支 只有一个if 没有其他的了)
如果你需要这个值,就把这个值放到for的最左边.
"""












