# ### python 操作mysql 
import pymysql
'''
# 1.基本语法
# (1) 连接数据库
# conn = pymysql.connect(host = "ip地址",user = "用户",password = "密码",database = "数据库",charset = "字符集",port = "端口号")
# 至少填写前4个参数
conn = pymysql.connect(host = "127.0.0.1",user = "root",password="123456",database = "db5",charset="utf8",port=3306)
# (2).创建游标对象,该对象执行sql相关方法
cursor = conn.cursor()
# (3).执行sql语句 
sql = "select * from employee"
# (如果是查询,返回查到的所有条数)
res = cursor.execute(sql)
print(res)
# (4) 获取查询出来的数据 fetchone 只获取一条数据
res = cursor.fetchone()
print(res)
#获取当前数据版版本号
res = cursor.execute("select version()")
print(res)
data = cursor.fetchone()
print("版本号",data)
# (5) 释放游标对象
# cursor.close()
# (6) 关闭数据库连接
conn.close()
'''


# 2.创建/删除 数据表
'''
conn = pymysql.connect(host = "127.0.0.1",user = "root",password="123456",database="db5")
# 创建游标对象 通过这个对象操作数据库
cursor = conn.cursor()
sql1 =  """
create table myt10(
id int unsigned primary key auto_increment,
first_name char(10) not null,
last_name char(10) not null,
age int unsigned,
sex tinyint,
money float
)
"""
# 准备sql语句
sql2 = "desc myt9"
# 执行sql语句
# cursor.execute(sql1)
cursor.execute(sql2)
# 获取一条数据
# data = cursor.fetchone()
# 获取所有数据
data = cursor.fetchall()
print(data) #('id', 'int(10) unsigned', 'NO', 'PRI', None, 'auto_increment')

try:
	# sql3 = "drop table myt1011111"
	sql3 = "drop table myt10"
	res = cursor.execute(sql3)
	print(res)
except:
	pass
print(33344)
# 释放游标对象
cursor.close()
# 关闭远程数据库连接
conn.close()
"""
(
	('id', 'int(10) unsigned', 'NO', 'PRI', None, 'auto_increment'), 
	('first_name', 'char(10)', 'NO', '', None, ''), 
	('last_name', 'char(10)', 'NO', '', None, ''), 
	('age', 'int(10) unsigned', 'YES', '', None, ''), 
	('sex', 'tinyint(4)', 'YES', '', None, ''), 
	('money', 'float', 'YES', '', None, '')
)
"""
'''

# (3)事务处理
# 1.基本语法
# 连接数据库
conn = pymysql.connect(host = "127.0.0.1",user = "root",password="123456",database = "db5",charset="utf8",port=3306)
# 创建游标对象,该对象执行sql相关方法
cursor = conn.cursor()
# 开启事务  通过pymysql 操作数据库,默认开启事务,需要最后通过commit进行提交数据;

sql1 = "begin"
sql2 = "select * from employee limit 3"
sql3 = "update employee set age = 39 where id = 3"
sql4 = "commit"
cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
# 最终需要通过commit提交事务,提交数据
cursor.execute(sql4)


# 释放游标对象
cursor.close()
# 关闭数据库连接
conn.close()





















