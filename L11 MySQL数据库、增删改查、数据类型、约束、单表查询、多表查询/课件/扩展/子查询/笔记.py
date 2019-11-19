# ### 补习:

# 先创建 class10 
	create table class10(id int unique ,classname varchar(255) );

# 创建student10
	create table student10(id int primary key auto_increment , name varchar(255),age int,class_id int);

# 给student10 添加外键 关联 class10当中 id
	alter table student10 add foreign key(class_id) references class10(id);

# 查询建表语句
	show create table student10\G

# 删除外键
	alter table student10 drop foreign key student10_ibfk_1;

# 删除外键之后,身上还存留一个普通的索引(这个索引就是单纯的加快查询速度)
	alter table student10 drop index class_id;



# ### order by 的使用
# 1. 查询所有员工信息，先按照age升序排序，如果age相同则按照hire_date降序排序
select * from employee order by age ,hire_date desc
# 2. 查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资升序排列
select post,avg(salary) from employee group by post having avg(salary) > 10000 
# 3. 查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资降序排列
# where + 子句 group by + 子句 having + 子句 order by + 子句 limit + 子句
select post,avg(salary) from employee group by post having avg(salary) > 10000 order by avg(salary) desc


# ### 多表之间的查询
	# 内连接(内联查询 inner join) : 两表或多表中条件同时满足,查询数据
	'''
	语法: select 字段 from 表1 inner join 表2 on 条件
	多表: select 字段 from 表1 inner join 表2 on 条件 inner join 表3 on 条件 inner join 表4 on 条件... ....
	'''
	
	select * from employee inner join department on employee.dep_id = department.id;
	# 用as 起别名 as 可以省略
	select * from employee as emp inner join department as dep on emp.dep_id = dep.id;
	select * from employee  emp inner join department  dep on emp.dep_id = dep.id;
	
	# 用普通的where 条件来写; 默认内联
	select * from employee emp,department dep where emp.dep_id = dep.id;
	
	# 外连接
		# (1) 左连接(左联查询left join) : 以左表为主,右表为辅,完整查询左表数据,右表对不上的补null
		"""语法: select 字段 from 表1 left join 表2 on 条件"""	
		select * from employee  emp left join department dep on emp.dep_id = dep.id
		
		# (2) 右连接(右联查询right join)
		"""语法: select 字段 from 表1 right join 表2 on 条件"""	
		select * from employee  emp right join department dep on emp.dep_id = dep.id
		# (3) 全连接(union)
		select * from employee  emp left join department dep on emp.dep_id = dep.id
		union
		select * from employee  emp right join department dep on emp.dep_id = dep.id
		
		# 例1:
		# 找出年龄大于25岁的员工以及员工所在的部门
		select employee.id,employee.name,department.name from employee inner join department on employee.dep_id = department.id where age > 25;		
		select employee.id,employee.name as ename,department.name as dname from employee inner join department on employee.dep_id = department.id where age > 25;		
		
		# 例2:
		# 以内连接的方式查询employee 和 department 表数据,以age字段升序排序; 
		# 方法1:
		select emp.id,emp.name,dep.name ,emp.age
		from employee as emp,department as dep
		where emp.dep_id = dep.id
		order by age asc;
		
		# 内联:
		select emp.id,emp.name,dep.name ,emp.age
		from employee as emp inner join department as dep
		on emp.dep_id = dep.id
		order by age desc;
		
		
		
	# 子查询:sql语句嵌套
	"""
		1.子查询是将一个查询语句嵌套在另一个查询语句中,用括号()包起来,表达一个整体
		2.一般应用在from  和 where 子句当中
		3.内层sql语句可以作为外层sql语句查询条件,也可以是表
		4.速度从快~ 慢 单表查询速度最快 > 其次是联表操作 > 子查询
		5.子查询中可以包含一些符号,> < >= <= == != is not in not in exists关键字 ....
	"""
	# (1)找出平均年龄大于25岁以上的部门;
	# 普通写法:
	select d.name,avg(age) from employee e,department d where e.dep_id = d.id group by d.name having avg(age)>25;
	
	# 内联写法:
	select dep_id,avg(age) 
	from employee emp inner join department dep 
	on emp.dep_id =dep.id
	group by dep.id
	having avg(age) > 25;
	
	select dep.name,avg(age) 
	from employee emp inner join department dep 
	on emp.dep_id =dep.id
	group by dep.name
	having avg(age) > 25;
	
	# 先帅选门平均年龄大于25岁的部门id
		select dep_id from employee group by dep_id having avg(age) > 25
	# 在按照结果赛选,选出id在201 和 202 之间的所有范围内数据
		select name from department where id in (201,202)
	# 最终子查询版本
		select name 
		from department 
		where id in (select dep_id from employee group by dep_id having avg(age) > 25);
		
	# (2)查看技术部门所有员工姓名;
	# 联表查询:
		select d.name,e.name from employee as e , department as d where e.dep_id = d.id and d.name="技术"
	# 内联查询:
		select d.name,e.name 
		from employee as e inner join  department as d 
		on e.dep_id = d.id 
		where d.name="技术";
	# 子查询
		(1)select id from department where name = "技术";
		(2)select name from employee dep_id = ?
		
		(3)select name from employee where dep_id = (select id from department where name = "技术")

	# (3) 查看哪个部门没员工?
		# 右联方法1
		select d.id,d.name from employee e right join department d on e.dep_id = d.id where e.dep_id is null
		
		# 子查询方法2
		# (1) 先来查询所有员工部门的种类
		select dep_id from employee group by dep_id;
		# (2) 查询department
		select id from department where id not in ?  
		# (3) 综合
		select id from department
		where id not in
		(select dep_id from employee group by dep_id)

	# (4)查询大于平均年龄的员工名与年龄
		# 假定平均年龄28岁
		# select * from 表 where age > 28
		
		# avg 聚合函数可以直接加在select 后面使用,如果放在其他字句后面,会要求分组group by
		# select * from employee where age > avg(age) error 
		
		select avg(age) from employee;
		# 先查询一下字句得到一个平均值,基于这个值在查询第二次
		select name , age 
		from employee
		where age > (select avg(age) from employee);


	# (5) 把大于其本部门平均年龄的员工名和姓名查出来
		# 计算本部门的平均值
		select dep_id, avg(age) from employee group by dep_id;

+----+------------+--------+------+--------+
| id | name       | sex    | age  | dep_id |  ? = age
+----+------------+--------+------+--------+
|  1 | egon       | male   |   18 |    200 |
|  2 | alex       | female |   48 |    201 |
|  3 | wupeiqi    | male   |   38 |    201 |
|  4 | yuanhao    | female |   28 |    202 |
|  5 | liwenzhou  | male   |   18 |    200 |
|  6 | jingliyang | female |   18 |    204 |
+----+------------+--------+------+--------+
		
		select * 
		from employee t1 inner join
		(select dep_id, avg(age) as age from employee group by dep_id) as t2
		on t1.dep_id = t2.dep_id
		where t1.age > t2.age
		'''
		
		from employee t1 inner join
		(select dep_id, avg(age) from employee group by dep_id) as t2
		on t1.dep_id = t2.dep_id     别名aaabbb
		看成一个整体,一整个数据表;
		然后单独拿出来,做类似于单表查询的动作;
		select * from aaabbb  where t1.age > t2.age
		'''

	# (6)查询每个部门最新入职的那位员工  
		# 每个部门都对应很多员工,每个员工有对应很多时间.这个时间如果最大就代表刚入职的;
		select post,max(hire_date) from employee group by post;
+----+------------+--------+-----+------------+-----------------------------------------+--------------+------------+--------+-----------+
| id | emp_name   | sex    | age | hire_date  | post                                    | post_comment | salary     | office | depart_id |  ????? 入职时间
+----+------------+--------+-----+------------+-----------------------------------------+--------------+------------+--------+-----------+
|  1 | egon       | male   |  18 | 2017-03-01 | 老男孩驻沙河办事处外交大使              | NULL         |    7300.33 |    401 |         1 |
|  2 | alex       | male   |  78 | 2015-03-02 | teacher                                 |              | 1000000.31 |    401 |         1 |   2015-03-02 
|  3 | wupeiqi    | male   |  81 | 2013-03-05 | teacher                                 | NULL         |    8300.00 |    401 |         1 |   2015-03-02 
|  4 | yuanhao    | male   |  73 | 2014-07-01 | teacher                                 | NULL         |    3500.00 |    401 |         1 |   2015-03-02 
|  5 | liwenzhou  | male   |  28 | 2012-11-01 | teacher                                 | NULL         |    2100.00 |    401 |         1 |  2015-03-02 
|  6 | jingliyang | female |  18 | 2011-02-11 | teacher                                 | NULL         |    9000.00 |    401 |         1 | 2015-03-02 
|  7 | jinxin     | male   |  18 | 1900-03-01 | teacher                                 | NULL         |   30000.00 |    401 |         1 |  2015-03-02 
|  8 | 成龙       | male   |  48 | 2010-11-11 | teacher                                 | NULL         |   10000.00 |    401 |         1 | 2015-03-02 
|  9 | 歪歪       | female |  48 | 2015-03-11 | sale                                    | NULL         |    3000.13 |    402 |         2 |
| 10 | 丫丫       | female |  38 | 2010-11-01 | sale                                    | NULL         |    2000.35 |    402 |         2 |    2017-01-27
| 11 | 丁丁       | female |  18 | 2011-03-12 | sale                                    | NULL         |    1000.37 |    402 |         2 |  2017-01-27
| 12 | 星星       | female |  18 | 2016-05-13 | sale                                    | NULL         |    3000.29 |    402 |         2 |  2017-01-27
| 13 | 格格       | female |  28 | 2017-01-27 | sale                                    | NULL         |    4000.33 |    402 |         2 |  2017-01-27
| 14 | 张野       | male   |  28 | 2016-03-11 | operation                               | NULL         |   10000.13 |    403 |         3 |
| 15 | 程咬金     | male   |  18 | 1997-03-12 | operation                               | NULL         |   20000.00 |    403 |         3 |
| 16 | 程咬银     | female |  18 | 2013-03-11 | operation                               | NULL         |   19000.00 |    403 |         3 |
| 17 | 程咬铜     | male   |  18 | 2015-04-11 | operation                               | NULL         |   18000.00 |    403 |         3 |
| 18 | 程咬铁     | female |  18 | 2014-05-12 | operation                               | NULL         |   17000.00 |    403 |         3 |
+----+------------+--------+-----+------------+-----------------------------------------+--------------+------------+--------+-----------+
select * 
from employee as t1 inner join
(select post,max(hire_date) as max_date from employee group by post) as t2
on t1.post = t2.post
where t1.hire_date = t2.max_date

	# (7)带EXISTS关键字的子查询
	'''
	exists 关键字表示存在
		如果内层sql能够查到数据,返回True ,外层sql执行查询操作
		如果内层sql不能查到数据,返回False,外层sql不执行查询操作.
	'''
	select * from employee 
	where exists
	(select * from department where id = 300)

	"""
	子查询可以单独作为一个字句,
	可以作为一个表,或者某个字段
	一般用在where 或者 from 或者 select 后面
	你想当成字段还是表要根据sql语句的编写形成
	通过查询出来的临时表可以和其他表在重新拼凑成一个更大的表
	然后把这个更大的表当成一个单表查询操作,完成任务;
	
	子查询一般都是在缺失某个字段的前提下或者缺失某些数据的时候,才被提出来的;
	可以灵活的进行自由拼凑达到目标;
	
	"""




































