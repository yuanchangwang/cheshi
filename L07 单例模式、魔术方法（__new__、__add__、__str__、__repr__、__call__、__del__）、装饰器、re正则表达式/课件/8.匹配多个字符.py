# ### 正则表达式 匹配多个字符
import re
# 量词练习
'''1) ? 匹配0个或者1个a '''
print(re.findall('a?b','abbzab abb aab'))  
'''2) + 匹配1个或者多个a '''
print(re.findall('a+b','b ab aaaaaab abb'))
'''3) * 匹配0个或者多个a '''
print(re.findall('a*b','b ab aaaaaab abbbbbbb'))
'''4) {m,n} 匹配m个至n个a '''
print(re.findall('a{1,3}b','aaab ab aab abbb aaz aabb'))


# 贪婪匹配 和 非贪婪匹配
"""

贪婪匹配:
	默认向更高次数匹配,程序当中默认使用贪婪匹配
非贪婪匹配:
	默认向更少次数匹配
	语法:只需要在量词的后面再加上一个?号
"""

strvar = "刘能和刘大脑袋和刘铁锥子12子3"
lst = re.findall("刘.",strvar)
print(lst)
# 贪婪匹配 
'''
底层用的时回溯算法:
从左到右开始寻找,直到找到最后再也找不到了,回头,找离右侧最近的那个值返回
'''
lst = re.findall("刘.?",strvar)
print(lst)
lst = re.findall("刘.+",strvar)
print(lst)
lst = re.findall("刘.*",strvar)
print(lst)
lst = re.findall("刘.*子",strvar)
print(lst)
lst = re.findall("刘.{1,20}",strvar)
print(lst)
lst = re.findall("刘.{1,20}子",strvar)
print(lst)

# 非贪婪匹配
lst = re.findall("刘.??",strvar)
print(lst)
lst = re.findall("刘.+?",strvar)
print(lst)
lst = re.findall("刘.*?",strvar)
print(lst)
lst = re.findall("刘.*?子",strvar)
print(lst)
lst = re.findall("刘.{1,20}?",strvar)
print(lst)
# 默认使用的是贪婪模式,一直找到最后一个子,如果使用非贪婪,找到第一个字就立刻返回.
lst = re.findall("刘.{1,20}?子",strvar)
print(lst)


# ###边界符练习 \b ^ $
# \b \bw 以w作为左边界  d\b 以d作为右边界
'''
\b 它默认是一个转义字符 退格 backspace 
需要通过字符串前面加上r,让转义字符失效,呈现正则的含义.
'''
lst = re.findall(r"d\b","word pwd abc")
print(lst)
lst = re.findall(r".*d\b","word pwd abc")
print(lst)
# 能够匹配到一个右边界d ,就立刻返回
# .可以匹配空白符,除了\n,剩下所有字符都能匹配到
lst = re.findall(r".*?d\b","word pwd abc")
print(lst)
lst = re.findall(r"\S*?d\b","word pwd abc") # 纯单词,舍去空格
print(lst)
lst = re.findall(r"\bw\S*","word pwd abc")  #'word'
print(lst)


# ### ^ $
"""
如果使用了^ 或者 $ 
^ : 必须以某个字符开头,后面剩下的无所谓
$ : 必须以某个字符结尾,前面剩下的无所谓
意味着把这个字符串当成一个整体
"""
strvar = "大哥大嫂大爷"

print(re.findall('大.',strvar))
print(re.findall('^大.',strvar)) # 只匹配一个,把字符串开成整体
print(re.findall('大.$',strvar)) # 只匹配一个,把字符串开成整体
# strvar = "大书"
print(re.findall('^大.$',strvar))
print(re.findall('^大.*?$',strvar))
print(re.findall('^g.*? ' , 'giveme 1gfive gay'))
print(re.findall('five$' , 'aassfive'))
print(re.findall("abc$","abcabcabc"))
print(re.findall('^giveme$' , 'giveme'))
print(re.findall('^giveme$' , 'giveme giveme'))
print(re.findall('^g.*?e$' , 'giveme giveme'))
print(re.findall('giveme' , 'giveme giveme'))
print(re.findall("^g.*e",'giveme 1gfive gay'))
print(re.findall("^g.*?e",'giveme 1gfive gay'))









