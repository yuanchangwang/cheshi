# ### os.path
#abspath()  将相对路径转化为绝对路径
'''
. 或者.. 代表的是相对路径
d: e: f: 这个具体的路径代表绝对路径
在linux里面 /开头的就是绝对路径 .或者..代表相对路径
'''
import os
res = os.path.abspath(".")  #D:\深圳周末三期\L006
print(res)

#basename() 返回文件名部分
strvar = r"D:\深圳周末三期\L006\aa.txt"
res = os.path.basename(strvar)
print(res) #aa.txt

#dirname()  返回路径部分
res = os.path.dirname(strvar)
print(res) #D:\深圳周末三期\L006

#split() 将路径拆分成单独的文件部分和路径部分 组合成一个元组
res = os.path.split(strvar)
print(res) #('D:\\深圳周末三期\\L006', 'aa.txt')

#join()  将多个路径和文件组成新的路径 
path1 = "home"
path2 = "wangwen"
path3 = "mysoft"
#可以自动通过不同的系统加不同的斜杠  linux / windows \
res = os.path.join(path1,path2,path3)
print(res) #home\wangwen\mysoft


#splitext() 将路径分割为后缀和其他部分
# 通过splitext 可以快速拿到一个路径中的后缀
strvar = r"D:\深圳周末三期\L006\aa.txt"
res = os.path.splitext(strvar)
print(res)

#getsize()  获取文件的大小
pathvar = r"D:\深圳周末三期\L006\1.内置函数.py"
res = os.path.getsize(pathvar)
print(res)

#isdir()    检测路径是否是一个文件夹(路径)
res = os.path.isdir(r'D:\深圳周末三期\L006')
print(res) #True
#isfile()   检测路径是否是一个文件
res = os.path.isfile(r'D:\深圳周末三期\L006\b.txt')
print(res) #True


#getctime() [windows]文件的创建时间,[linux]权限的改动时间(返回时间戳)
res = os.path.getctime(r"D:\深圳周末三期\L006\b.txt")
print(res)
import time
res = time.ctime(1557649965)
print(res)  #Sun May 12 16:32:45 2019


#getmtime() 获取文件最后一次修改时间(返回时间戳)
res = os.path.getmtime(r"D:\深圳周末三期\L006\b.txt")
res = time.ctime(res)
print(res)


#getatime() 获取文件最后一次访问时间(返回时间戳) # 存在系统差异
res = os.path.getatime(r"D:\深圳周末三期\L006\b.txt")
res = time.ctime(res)
print(res)

#exists()   检测指定的路径是否存在
res = os.path.exists(r"D:\深圳周末三期\L006\b.txt")
print(res)

print("<====>")
#isabs()    检测一个路径是否是绝对路径 (了解)
strvar  =  "."
# strvar = r"D:\深圳周末三期\L006\b.txt"
res = os.path.isabs(strvar)
print(res)
















