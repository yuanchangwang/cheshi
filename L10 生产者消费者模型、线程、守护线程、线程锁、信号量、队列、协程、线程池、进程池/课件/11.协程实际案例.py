# ### 协程的例子
"""
# (1)spawn(函数,参数1,参数2,参数3....) 启动切换一个协程
# (2)join() 阻塞,直到某个协成执行完毕
# (3)joinall() 等待所有协成执行任务完毕
	1.g1.join()  g2.join() 可以通过joinall简写
	2.gevent.joinall( [g1,g2]  ) 等价于 1; 参数是一个列表;
# (4)value 获取协成返回值
"""


'''
# 如果想把两句代码放在一行里面写,中间用分号;隔开
a = 1;b = 2
print(a,b)
'''
# (1) joinall value 这两个函数的用法
'''
from gevent import monkey;monkey.patch_all()
import time
import gevent

def eat():
	print("eat one")
	time.sleep(1)
	print("eat two")
	return "吃完了"


def play():
	print("play one")
	time.sleep(1)
	print("play two")
	return "玩完了"

g1 = gevent.spawn(eat)
g2 = gevent.spawn(play)

gevent.joinall( [g1,g2]  )
# 获取协成的返回值
print(g1.value)
print(g2.value)


print("主线程结束.")
'''

# (2) 利用协程爬取页面数据
import gevent
import requests
import time
"""
HTTP 状态码:
	200 ok
	400 Bad Request
	404 Not Found
"""
# 抓取网站信息,返回响应对象
response = requests.get("http://www.baidu.com")
print(response)
# 获取状态码
res = response.status_code
print(res)
# 获取字符编码集 apparent_encoding
res_code = response.apparent_encoding
print(res_code)
# 设置编码集
response.encoding = res_code
# 获取网页里面的内容
res = response.text
print(res)

"""
# 用消费者生产者模型扒网址
import re
strvar = r'<img hidefocus=true src="https://www.baidu.com/img/bd_logo1.png"  width=270 height=129>'
obj = re.search("src=(.*?) ",strvar)
res = obj.group()
res = obj.groups()[0]
"""
 

url_list = [
"http://www.baidu.com",
"http://www.4399.com",
"http://www.7k7k.com",
"http://www.jingdong.com",
"http://www.taobao.com",
"http://www.baidu.com",
"http://www.4399.com",
"http://www.7k7k.com",
"http://www.jingdong.com",
"http://www.taobao.com",
"http://www.baidu.com",
"http://www.4399.com",
"http://www.7k7k.com",
"http://www.jingdong.com",
"http://www.taobao.com",
"http://www.baidu.com",
"http://www.4399.com",
"http://www.7k7k.com",
"http://www.jingdong.com",
"http://www.taobao.com",
"http://www.baidu.com",
"http://www.4399.com",
"http://www.7k7k.com",
"http://www.jingdong.com",
"http://www.taobao.com",
"http://www.baidu.com",
"http://www.4399.com",
"http://www.7k7k.com",
"http://www.jingdong.com",
"http://www.taobao.com",
"http://www.baidu.com",
"http://www.4399.com",
"http://www.7k7k.com",
"http://www.jingdong.com",
"http://www.taobao.com",
"http://www.baidu.com",
"http://www.4399.com",
"http://www.7k7k.com",
"http://www.jingdong.com",
"http://www.taobao.com",
"http://www.baidu.com",
"http://www.4399.com",
"http://www.7k7k.com",
"http://www.jingdong.com",
"http://www.taobao.com",
"http://www.baidu.com",
"http://www.4399.com",
"http://www.7k7k.com",
"http://www.jingdong.com",
"http://www.taobao.com",
"http://www.baidu.com",
"http://www.4399.com",
"http://www.7k7k.com",
"http://www.jingdong.com",
"http://www.taobao.com",
"http://www.baidu.com",
"http://www.4399.com",
"http://www.7k7k.com",
"http://www.jingdong.com",
"http://www.taobao.com",
"http://www.baidu.com",
"http://www.4399.com",
"http://www.7k7k.com",
"http://www.jingdong.com",
"http://www.taobao.com",
"http://www.baidu.com",
"http://www.4399.com",
"http://www.7k7k.com",
"http://www.jingdong.com",
"http://www.taobao.com",
"http://www.baidu.com",
"http://www.4399.com",
"http://www.7k7k.com",
"http://www.jingdong.com",
"http://www.taobao.com",
"http://www.baidu.com",
"http://www.4399.com",
"http://www.7k7k.com",
"http://www.jingdong.com",
"http://www.taobao.com",
]

def get_url(url):
	response = requests.get(url)
	if response.status_code == 200:
		pass
		# print(response.text)

# (1) 正常方式爬取数据
startime = time.time()
for i in url_list:
	get_url(i)
endtime = time.time()
print("<====1>")
print(endtime-startime,"<1111>") #13.869777202606201 <1111>

# (2) 用协程爬取数据 更快
startime = time.time()
lst = []
for i in url_list:
	g = gevent.spawn(get_url,i)
	lst.append(g)

gevent.joinall(lst)
endtime = time.time()
print("<====2>")
print(endtime - startime,"<2222>") #11.696096658706665 <2222>
# 5.723864316940308 <2222>
# 6.224448204040527 <2222>











