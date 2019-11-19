# ### python 操作mysql 增删改
import pymysql
"""
	通过pymysql这个模块提交给mysql 服务器,默认开启事务
	事务处理,必须要依赖commit来进行提交数据,也可以用rollback回滚到开始时候 的数据
	不提交数据,默认回滚
		
	提交数据 conn.commit()
	回滚数据 conn.rollback()
	
	execute executemany 如果执行的是增删改,返回的是受影响的行数
	execute 如果执行的是查,返回的是查询到的数量;
"""

# 连接数据库
conn = pymysql.connect(host="127.0.0.1",user="root",password="123456",database="db5")
# cursor=pymysql.cursors.DictCursor 把返回的数据变成字典,默认是元组;
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 1.增
# 执行sql语句
sql = """insert into myt9(first_name,last_name,age,sex,money) values(%s,%s,%s,%s,%s)"""

# execute只执行一条数据
res = cursor.execute( sql,( "马","巨强",74,1,8) )
# print(res)
# executemany执行多条数据 返回第一次插入的那条数据的id
# res = cursor.executemany(  sql, [("张","过程",88,0,2),("意","四",13,1,90),("罗","婷",18,1,100000),("黄","胸大",20,0,900)]  )
# print(res)

# 获取最后一条插入数据的id(一般常用订单号上)
print(cursor.lastrowid)




# 2.删
"""
sql = "delete from myt9 where id = %s "
res = cursor.execute(sql,(5))

if res:
	print("删除成功")
else:
	print("删除失败")
"""

# 3.改
"""
sql = "update myt9 set first_name = %s where  id = %s"
res = cursor.execute(sql,("王",9))
if res:
	print("修改成功")
else:
	print("修改失败")
"""

# 4.查 返回搜索的条数
sql2 = "select * from myt9"
res = cursor.execute(sql2)
print(res)
# 查询一条 fetchone()
data = cursor.fetchone()
print(data)

# 查询多条 fetchmany(查询的条数) 默认查一条,基于上一条查询,往下在查查2条
data = cursor.fetchmany(2) 
print(data)

# 查询所有数据
data = cursor.fetchall()
print(data)
#[{'id': 9, 'first_name': '王', 'last_name': '巨强', 'age': 74, 'sex': 1, 'money': 8.0}]

for row in data:
	first_name = row['first_name']
	last_name = row['last_name']
	age = row['age']
	if row['sex'] == 0:
		sex = "男"
	else:
		sex = "女"
	money = row['money']
	
	print("姓:{},名字:{},性别:{},年龄:{},收入:{}".format(first_name,last_name,sex,age,money))


# 可以选择查询的位置
sql3 = "select * from myt9 where id >= 20"
res = cursor.execute(sql3)
print(res)
data = cursor.fetchone()
print(data)

# 相对当前位置进行移动
cursor.scroll(7,mode="relative")  # 向后移动
print(cursor.fetchone())
cursor.scroll(-5,mode="relative") # 向前移动
print(cursor.fetchone())

# 绝对位置移动
cursor.scroll(0,mode="absolute")
print(cursor.fetchone())







conn.commit()

cursor.close()
conn.close()











































