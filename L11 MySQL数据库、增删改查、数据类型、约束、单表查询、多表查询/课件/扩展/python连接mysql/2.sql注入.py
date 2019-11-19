import pymysql
""""""
# 1.sql 注入的问题
user = input("user>>:").strip()
pwd = input("password>>:").strip()
# sdfsd' or 1=1 -- sfdksjk
conn= pymysql.connect(host="127.0.0.1",user="root",password="123456",database="db5",charset="utf8",port=3306)
cursor = conn.cursor()
sql = "select * from usr_pwd where username = '%s'  and password = '%s' " % (user,pwd)
print(sql) #select * from usr_pwd where username = 'iuiuuyuy' or 1=1 -- sdfsdfs'  and password = '' 
res = cursor.execute(sql)
print(res)

if res:
	print("登录成功!")
else:
	print("登录失败~")

# 释放游标对象
cursor.close()
# 关闭数据库连接
conn.close()


''''''
# 2.解决办法:
# 如果想用execute 的预处理功能 %s 不要在套一层引号了,但是如果是字符串的格式化,必须加引号.
user = input("user>>:").strip()
pwd = input("password>>:").strip()

conn= pymysql.connect(host="127.0.0.1",user="root",password="123456",database="db5",charset="utf8",port=3306)
cursor = conn.cursor()
sql = 'select * from usr_pwd where username = %s  and password = %s '

# execute可以提前过滤sql语句,做一下预处理.方式sql注入.
print(sql)
res = cursor.execute(sql,(user,pwd))
if res:
	print("登录成功")
else:
	print("登录失败")


# 释放游标对象
cursor.close()
# 关闭数据库连接
conn.close()


























