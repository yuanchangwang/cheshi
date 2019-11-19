# ### random 随机模块
import  random
#random() 获取随机0-1之间的小数(左闭右开)  0<= x < 1
res = random.random()
print(res)

#randrange() 随机获取指定范围内的整数(包含开始值,不包含结束值,间隔值)
res = random.randrange(3)  # 0~2
print(res)
res = random.randrange(1,10) # 1~9
print(res)
res = random.randrange(1,10,3) # 1 4 7 
print(res)

#randint()   随机产生指定范围内的随机整数 (目前唯一可以取到最大值的函数,不推荐使用)
res = random.randint(2,5) # 2 3 4 5 最大值可以取到
print(res)
print('<===>')
# randint 必须给2个参数 1个或者3个都不行,功能有局限性,不推荐使用
# res = random.randint(2,5,2)
# print(res)


#uniform() 获取指定范围内的随机小数(左闭右开)
res = random.uniform(1,10) # 1<= x < 10
print(res)
res = random.uniform(5,-3)
print(res)
'''
a = 5
b = -3
return a + (b-a) * self.random()
5+ (-3-5) * (0<=x<1)
5+ (-8) * (0<=x<1)
最大值 5
最小值 -3
-3 < x <=5
'''


#choice()  随机获取序列中的值(多选一)
listvar = [1,2,3,90,6,5]
res = random.choice(listvar)
print(res)

# 自定义函数 实现choice的效果
def mychoice():
	length = len(listvar)
	res = random.randrange(0,length) # 0 ~ 5
	return  listvar[res]
print(mychoice())

#sample()  随机获取序列中的值(多选多) [返回列表]
# sample(容器类型数据,选几个)
listvar = ["周杰伦","李宇春","王宝强","宋小宝","刘德华","张学友","王文"]
res = random.sample(listvar,2)
print(res)


#shuffle() 随机打乱序列中的值(直接打乱原序列)
listvar = ["周杰伦","李宇春","王宝强","宋小宝","刘德华","张学友","王文"]
random.shuffle(listvar)
print(listvar)

print('<===>')
# 实现一个验证码功能 每次随机产生5个字符
'''a-z A-Z 0-9'''
def yanzhengma():
	strvar = ''
	for i in range(5):
		# res = chr(97)
		# a-z 范围的小写字母
		a_z = chr(random.randrange(97,123))
		# A-Z 产生所有的大写字母 65 => A  90
		A_Z = chr(random.randrange(65,91))
		# 0-9 产生0-9 10个数字
		num  = str(random.randrange(0,10)) # 为了实现字符串的拼接
		# 把范围的可能出现的字符放到同一的列表中进行随机挑选
		listvar = [a_z,A_Z,num]
		# 把选好的5个随机字符 通过+来形成拼接
		strvar += random.choice(listvar)
	# 直接返回该字符串
	return strvar
res = yanzhengma()
print(res)






