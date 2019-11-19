# ### time 时间模块

#time()      获取本地时间戳
import time
res = time.time()
print(res)

#mktime()        通过[时间元组]获取[时间戳] (参数是时间元组)
ttl = (2019,5,12,15,21,0,0,0,0)
res = time.mktime(ttl)
print(res)

#localtime()     通过[时间戳]获取[时间元组] (默认当前时间)
ttl = time.localtime()  # 默认使用当前时间戳
print(ttl)
ttl = time.localtime(1557645000) # 自定义时间戳,转化为时间元组
print(ttl)
'''
time.struct_time(
tm_year=2019, 
tm_mon=5, 
tm_mday=12, 
tm_hour=15, 
tm_min=23, 
tm_sec=53, 
tm_wday=6,   0~ 6 0代表周一 6 代表周日 
tm_yday=132, 
tm_isdst=0)
'''
#ctime()         通过[时间戳]获取[时间字符串] (默认当前时间)
res = time.ctime()  # 默认使用当前时间戳
print(res)  
res = time.ctime(1557645000) # 可以手动自定义时间戳
print(res)

#asctime()       通过[时间元组]获取[时间字符串](参数是时间元组)
# ttl = (2019,5,12,15,21,0,1,0,0)
# res = time.asctime(ttl)
# print(res)

# 优化版 (推荐使用)
'''
ttl = (2019,5,12,15,21,0,4,0,0)
res = time.mktime(ttl)
print(time.ctime(res))
'''
print("<1122>")
#strftime()      通过[时间元组]格式化[时间字符串]  (格式化字符串,[可选时间元组参数])
res = time.strftime("%Y-%m-%d %H:%M:%S") # 默认以当前时间戳转化为字符串
print(res)
# linux当中 strftime可以识别中文,windows不行
res = time.strftime("%Y-%m-%d %H:%M:%S",(2008,8,8,8,8,8,0,0,0))
print(res)


#strptime()      通过[时间字符串]提取出[时间元组]  (时间字符串,格式化字符串)
# 注意:左右两侧的字符串要严丝合缝,有多余的空格都不行,然后按照次序,依次通过格式化占位符,提取时间
res = time.strptime("2019年3月8号15点21分30秒,发射了人造卫星嫦娥"  ,  "%Y年%m月%d号%H点%M分%S秒,发射了人造卫星嫦娥")
print(res)
'''
time.struct_time(
tm_year=2019, 
tm_mon=3,
 tm_mday=8,
 tm_hour=15, 
 tm_min=21, 
 tm_sec=30,
 tm_wday=4, 
 tm_yday=67,
 tm_isdst=-1)

'''
#sleep()         程序睡眠等待
# time.sleep(30)
# print(11233434)

#perf_counter()  用于计算程序运行的时间
startime = time.perf_counter()
print(startime)
for i in range(1000000000):
	pass
endtime = time.perf_counter()
# 结束时间  - 开始时间[ time.time()] 也可以实现;
res = endtime - startime
print(res)





















