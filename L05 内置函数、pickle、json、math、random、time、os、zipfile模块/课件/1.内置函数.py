# ### 内置函数

# abs    绝对值函数
res = abs(-9.9867)
print(res)

# round  四舍五入 (n.5 n为偶数则舍去 n.5 n为奇数，则进一!)
'''奇进偶不进'''
# res = round(4.5)
res = round(3.5)
res = round(12.5)
print(res)

# sum    计算一个序列得和
listvar = [1,2,34,34,43,32,5]
total = 0
for i in listvar:
	total += i
print(total)

res = sum(listvar)
print(res)

# max    获取一个序列里边的最大值
listvar = [1,2,34,34,43,32,5]
res = max(listvar)
print(res)

# min    获取一个序列里边的最小值
'''
# sort 找出最大值和最小值
listvar.sort()
print(listvar)
res_min = listvar[0]
res_max = listvar[-1]
print(res_min)
print(res_max)
'''
listvar = [1,2,34,34,43,32,5]
res = min(listvar)
print(res)

# 找出岁数最小的元组
listvar = [("张三",45),("李四",38),("王五",18),("田七",120)]
def func(n):
	#("张三",45)
	return n[-1]
res = min(listvar,key=func)
print(res)
'''
("王五",18 扔到func当中  return 18
首先把("张三",45) 扔到func当中  return 45
("李四",38) 扔到func当中  return 38
("田七",120)  扔到func当中  return 120
按照右侧实际年龄进行排序,找出最小的那个数,直接把元组返回.
'''

# pow    计算某个数值的x次方
res = pow(2,3)
res = pow(4,20)
'''pow(可以接受第三个可选参数 , 第三个参数是用来取余的)'''
res=  pow(2,3,3)
print(res)
'''
-7 4
res = -7 % -4
print(res)
'''
# range  产生指定范围数据的可迭代对象
res = range(10)
print(res)
for i in range(10):
	print(i)
for i in range(1,8):
	print(i)
for i in range(1,16,3):
	print(i)

for i in range(10,0,-1):
	print(i)

# bin    将10进制数据转化为二进制
res = bin(15)
print(res)
# oct    将10进制数据转化为八进制
res = oct(8)
print(res)
# hex    将10进制数据转化为16进制
'''
9 1001
a 1010
b 1011
c 1100
d 1101
e 1110
f 1111
'''
res = hex(16)
print(res)


# chr    将ASCII编码转换为字符
res  = chr(97)
print(res)
# ord    将字符转换为ASCII编码
res = ord("A")
print(res)

# eval   将字符串当作python代码执行
res = "print(123)"
res = "print('sdfsdf')"
res = "print(\"sdfsdf\")"
print(res)
eval(res)

# exec   将字符串当作python代码执行(功能更强大)
res = """
for i in range(10):
	print(i)
"""
# 要注意小心sql注入 delete from 数据 where id = 1 exec或者eval两个函数慎用
exec(res)


# repr   不转义字符输出字符串
listvar = [1,2,3]
res = repr(listvar)
print(res,type(res))
strvar = "123"
print(repr(strvar))
strvar = "111\n\t\r"
print(repr(strvar))

# input  接受输入字符串
# res = input("请输入您的用户名:")
# print(res,type(res))

# hash   生成哈希值
'''
字典的键 和 集合当中的值 需要使用哈希算法
哈希算法在存储上是无序的散列,经过计算之后会产生具有固定长度的唯一值
'''
# 通过字符串和内存地址加在一起计算出来的 通过hash计算出来
res1 = "今天天气好"
res2 = "今天天气好"
res3 = "132"
print(hash(res1))
print(hash(res2))
print(hash(res3))
'''
可哈希数据:Number(int bool complex float) str () [不可变数据]
不可哈希数据:dict list set [可变数据]
'''





