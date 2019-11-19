# ### 序列化模块 pickle
'''
序列化:把不能够直接存储的数据变成可存储的过程就是序列化
反序列化:把储存的数据拿出来恢复成原来的数据类型就是反序列化

php:
serialize
unserialize
'''
# import 引入模块  引入pickle模块
import pickle
#dumps 把任意对象序列化成一个bytes
dic = {"a":1,"b":2}
res = pickle.dumps(dic)
print(res)
#loads 把任意bytes反序列化成原来数据
res = pickle.loads(res)
print(res,type(res))

# 函数可以序列化么?
def func():
	print("我是一个函数")
res = pickle.dumps(func)
print(res)
print("<==>")
res = pickle.loads(res)
res()

# 迭代器可以序列化么?
from collections import Iterator,Iterable
it = iter(range(10))
print(isinstance(it,Iterator))
res = pickle.dumps(it)
print(res)
res = pickle.loads(res)
print(res)
for i in range(3):
	print(next(res))

# 所有的数据类型都可以通过pickle进行序列化



#dump  把对象序列化后写入到file-like Object(即文件对象)
dic = {"a":1,"b":2}
with open("0512_1.txt",mode="wb") as fp:
	# pickle.dump(数据类型,文件对象) 先把数据变成二进制字节流 在存储在文件当中
	pickle.dump(dic,fp)

#load  把file-like Object(即文件对象)中的内容拿出来,反序列化成原来数据
with open("0512_1.txt",mode="rb") as fp:	
	res = pickle.load(fp)
print(res)

































