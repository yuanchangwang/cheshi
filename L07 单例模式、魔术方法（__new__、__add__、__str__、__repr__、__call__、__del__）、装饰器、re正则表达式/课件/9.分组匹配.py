# ### 正则表达式 
# 分组练习
import re
'''
# 1.正常分组 （）
1) 正常情况下用()圆括号进行分组 可以用\1 反向引用第一个圆括号匹配的内容。
2) (?:正则表达式) 表示取消优先显示的功能
'''

print(re.findall('.*?_good','wusir_good alex_good xboyww_good')) #['wusir_good', ' alex_good', ' xboyww_good']
# 匹配所有的姓名
print(re.findall('(.*?)_good','wusir_good alex_good xboyww_good')) #['wusir', ' alex', ' xboyww']
print(re.findall('(?:.*?)_good','wusir_good alex_good secret男_good'))


# a|b 匹配字符a 或者 匹配字符b  把字符串长的写在前面,字符串短的写在后面
# | 代表或的意思
res = re.findall("abcd|abc","abcdabcdabcd abc")
print(res)

# 匹配小数  3.14 .34 35. ... 2.41 .3 34..
strvar = " 3.14 .34 35. ... 2.41.3 34.."
res  = re.findall("\d+\.\d+",strvar)
print(res)

# 匹配小数和整数 
strvar = "3.15 34 .. 3434.23.234.2323 .34.34 .3434 .. .. nihao"
res = re.findall("\d+\.\d+|\d+",strvar)
print(res)
# 优化版 
# findall 这个函数默认优先显示小括号里面的内容,如果不想显示,用?:
# 小括号代表的是分组,放到一起代表整体,这个例子要么出现小数点和后面的值,要么不出现.
res = re.findall("\d+(?:\.\d+)?",strvar)
print(res)

# 匹配135或171的手机号 
res = re.findall("(?:135|171)\d{8}","13588889897 17180668088")
print(res)

# 正则要求卡主开头和结尾,且长度是11位 (这个例子开头结尾满足,但长度不对)
res = re.findall("(?:^135|^171)\d{8}$","13588889897 17180668088")
print(res)
#(?:     ^135      |      ^171     )
res = re.findall("(?:^135|^171)\d{8}$","17188889897")
print(res)


# ### search 正则方法 
"""
search("正则表达式","要匹配的字符串")
它返回的是一个对象,

对象.属性
对象.方法()
想要获取对象里面的值用group()方法 
想要获取分组里面的值用groups()方法

区别于findall 
findall 找出所有匹配的结果,从左到右,返回的是列表
search  找出一个结果就返回,从左到右,返回的是对象
"""
obj = re.search("\d+","ksjdfks898sdf*&*&  78787878")
print(obj)
res = obj.group() #898
print(res)

# 匹配www.baidu.com 或者 www.oldboy.com
obj = re.search("(www).(baidu|oldboy).(com)","www.baidu.com www.oldboy.com")
# 优点1:通过group 拿到实际匹配到的内容
res = obj.group()
print(res) #www.baidu.com
# 优点2:通过groups 拿到小括号里面匹配到的内容
res = obj.groups()
print(res)
# 结论:同一时间,既可以拿到匹配的结果,又可以拿到小括号里的内容,而findall不具备.
# findall 同一时间只能拿取一种结果,要么是实际匹配的,要么是小括号的.
# search 只能匹配一个, findall 可以匹配所有. 这是两个函数之间的差别.

# 优先显示了圆括号里面的内容
res = re.findall("(www).(baidu|oldboy).(com)","www.baidu.com www.oldboy.com")
# www.baidu.com  ('www', 'baidu', 'com')
# www.oldboy.com ('www', 'oldboy', 'com')
print(res) 


# 用来对比两个函数区别
# 匹配出5*4 或者 6/8
strvar = "5*4+6/8"
obj = re.search("\d+[*/]\d+",strvar)
# 获取对象当中的值
res = obj.group()
print(res)

res= re.findall("\d+[*/]\d+",strvar)
print(res)

# 一般有分组的情况下用search 更多,找到所有匹配条件一般用findall








































