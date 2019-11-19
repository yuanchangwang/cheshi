# ### json 
'''
json 的功能也是序列化,不过他序列化的最终结果是一个字符串
不同的语言之间,进行数据交流都使用json数据格式
所有语言都能够识别的数据格式叫做json ,json数据格式
python 中能够使用json格式的数据类型 只有如下:
int float bool str list tuple dict None  [不包含complex set]

语言和语言之间的交流用json(字符串)
数据之间的传输和存储用pickle(二进制字节流)
'''
# 第一对 dumps 和 loads 把数据序列化或者反序列化成字符串
'''
ensure_ascii=True (默认值) 如果想要显示中文 如下:ensure_ascii = False
sort_keys=False  对字典的键进行排序 (会按照ascii 字符的从小到大进行排序)
'''


import json
dic = {"name":"刘铁蛋","age":18,"sex":"女性","family":["father","妈妈"],"agz":1}
res = json.dumps(dic,ensure_ascii=False,sort_keys=True)
print(res,type(res))
'''
{
"name": "\u5218\u94c1\u86cb", 
"age": 18, 
"sex": "\u5973\u6027", 
"family": ["father", "\u5988\u5988"]} 
<class 'str'>
'''
# 第二对 dump  和 load  应用在数据的存储的转化上
dic = {"name":"刘铁蛋","age":18,"sex":"女性","family":["father","妈妈"],"agz":1}
with open("0512_2.txt",mode="w",encoding="utf-8") as fp:	
	json.dump(dic,fp,ensure_ascii=False)

with open("0512_2.txt",mode="r",encoding="utf-8") as fp:
	res = json.load(fp)
print(res,type(res))

# pickle  和 json 之间的用法区别
'''
json 可以连续dump , 但是不能连续load , load是一次性拿出所有数据而不能识别.
可以使用loads ,一行一行的读取,一行一行的通过loads来转化成原有数据类型
'''
# (1) json
dic = {"name":"刘铁蛋","age":18,"sex":"女性","family":["father","妈妈"],"agz":1}
with open("0512_3.txt" , mode="w",encoding="utf-8") as fp:
	json.dump(dic,fp)
	fp.write('\n')
	json.dump(dic,fp)
	fp.write('\n')

print("<===>")
with open("0512_3.txt" ,mode="r",encoding="utf-8") as fp:
	# load 是一次性把所有的数据拿出来,进行识别
	# load 不能识别多个数据混在一起的情况
	# 用loads 来解决load 不能识别多个数据的情况
	# res = json.load(fp)  
	for  i  in fp:
		# print(i,type(i))
		res = json.loads(i)
		print(res,type(res))
	
# print(res)
print("<=====>")
# (2) pickle
dic = {"name":"刘铁蛋","age":18,"sex":"女性","family":["father","妈妈"],"agz":1}
import pickle
with open("0512_4.txt",mode="wb") as fp:
	pickle.dump(dic,fp)
	pickle.dump(dic,fp)
	pickle.dump(dic,fp)
	pickle.dump(dic,fp)
print("<===123==>")
with open("0512_4.txt",mode="rb") as fp:
	'''
	res = pickle.load(fp)
	print(res)
	res = pickle.load(fp)
	print(res)
	res = pickle.load(fp)
	print(res)
	res = pickle.load(fp)
	print(res)
	'''
	try:
		while True:
			res = pickle.load(fp)
			print(res)
	except:
		pass
'''
try:
	...
except:
	...
把有问题的代码赛到try 代码块当中
如果发生异常报错,直接执行except其中的代码块
优点:不会因为报错终止程序运行	
try:
	listvar = [1,2]
	print(listvar[15])
except:
	pass
'''

"""
# json 和 pickle 两个模块的区别:
(1)json序列化之后的数据类型是str,所有编程语言都识别,
   但是仅限于(int float bool)(str list tuple dict None)
   json不能连续load,只能一次性拿出所有数据
(2)pickle序列化之后的数据类型是bytes,
   所有数据类型都可转化,但仅限于python之间的存储传输.
   pickle可以连续load,多套数据放到同一个文件中

"""

















































