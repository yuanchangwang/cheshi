# ### 正则表达式  匹配单个字符
import re
# findall("正则表达式","要匹配的字符串")

# \d 和 \D
'''
\d 匹配数字
\D 匹配非数字
'''
lst = re.findall("\d","sdfsdafjaskldfjkls 8989asda神秘男孩^&^&*^&*")
print(lst)
lst = re.findall("\D","sdfsdafjaskldfjkls 8989asda神秘男孩^&^&*^&*")
print(lst)

"""
\w 匹配字母数字下换线 (正则函数中,支持中文匹配)
\W 匹配非字母,数字,下划线
"""
lst = re.findall("\w","829348sdfhjks_dhjsdf你好神秘&*&*大佛...&*&*")
print(lst)
lst = re.findall("\W","829348sdfhjks_dhjsdf你好神秘&*&*大佛...&*&*")
print(lst)

'''
\s 匹配任意的空白符(\n \t)
\S 匹配任意的非空白符
'''
strvar = ' 					'
lst = re.findall("\s",strvar)
print(lst)
strvar = "  8989sdf 	111"
lst = re.findall("\S",strvar)
print(lst)

'''
\n 匹配一个换行
\t 匹配一个缩进
'''
strvar = """
sdfsd   sdfsdf   sfsdfsdf
sdfsddffg 	dfgdfg	fgdfg
"""
lst = re.findall("\n",strvar)
print(lst)
lst = re.findall("\t",strvar)
print(lst)

# ### 字符组 [123]
'''
[123] 必须从字符组当中挑出一个出来,个数上有要求,必须一个,如果匹配不到就是空.
'''
lst = re.findall("[123]","sdfs3fkj5kj")
print(lst)

print(re.findall('a[abc]b','aab abb acb adb'))
# [0123456789] => [0-9] -是一个特殊字符,代表范围0-9 0到9
print(re.findall('a[0123456789]b','a1b a2b a3b acb ayb'))
print(re.findall("a[0-9]b",'a1b a2b a3b acb ayb'))

#[abcdefg] => [a-g] 表达所有小写字符可以用[a-z]
print(re.findall('a[a-z]b','a1b a2b a3b acb ayb adb')) #['acb', 'ayb', 'adb']
# print(re.findall('a[abcdefg]b','a1b a2b a3b acb ayb adb')) #['acb', 'adb']

# [ABCDEFG] A-G  [A-Z]用来表达所有大写字符
print(re.findall('a[A-Z]b','a1b a2b a3b  aAb aDb aYb')) #['aAb', 'aDb', 'aYb']
print(re.findall('a[ABCDEFG]b','a1b a2b a3b  aAb aDb aYb')) #aAb aDb


print(re.findall('a[0-9a-zA-Z]b','a-b aab aAb aWb aqba1b'))  #['aab', 'aAb', 'aWb', 'aqb', 'a1b']
print(re.findall('a[0-9][*#/]b','a1/b a2b a29b a56b a456b')) #['a1/b']
# 字符组当中的^ 代表除了的意思
# 除了+ - * / 这些字符之外,剩下的都能匹配
print(re.findall('a[^-+*/]b',"a%b ccaa*bda&bd")) #['a%b', 'a&b']
# 在特殊字符前面加商一个\,让原本有意义的字符变得无意义,用于正则字符匹配
print(re.findall('a[\^]b',"a^b")) #['a%b', 'a&b']





