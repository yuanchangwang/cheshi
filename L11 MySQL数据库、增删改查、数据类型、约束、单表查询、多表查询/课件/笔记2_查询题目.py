# ### 1.单表查询 
	# 一.where 条件表达式 
		#1.作用:对表中的数据进行筛选
		#2.对值进行判断
		= > >= < <= != <>(不等于)
		#3.判断一个值得范围between 小值 and 大值 [小值,大值] 在两者之间取值
		   in(值1,值2,值3) 在括号里这个范围
		#4.like 模糊查询 like "%" 通配符 陪陪任意长度的任意字符
			like "%a" 以a结尾的任意长度字符串
			like "a%" 以a开头的任意长度字符串
			like "%a%"匹配中间带个a的字符串
			like "_a" 一共2个长度,以a结尾,什么字符无所谓
			like "a__"一共3个长度,以a开头,后面2个字符是什么无所谓.
		#5.多个条件拼接
			and 两个条件拼接一起,都成立才成立
			or  两个条件拼一起,有一个成立即成立
			not 非,取反或为真或为假
	
		# (1) 单条件查询:
			# 查询部门是sale的所有员工姓名;
			select emp_name from employee where post="sale";
			
		# (2) 多条件查询
			# 部门是teacher,收入大于10000所有字段
			select * from employee where post="teacher" and salary>10000;
			
		# (3) 关键字 between .. and ..
			# 收入在1万和2万之间的姓名收入
			select emp_name,salary from employee where salary between 10000 and 20000;
			# 收入不再1万和2万之间的姓名收入
			select emp_name,salary from employee where salary not  between 10000 and 20000;
			
		# (4) 关键字is null(判断某个字段是否为null 不能用等号 用is)
			# 查询post_comment 是空的
			select * from employee where post_comment is null;
			select * from employee where post_comment is not  null;
			
			# 设置字符串的""空 和 类型上的null 不一样,null更像是一个占位,什么数据也没有;
			update employee set post_comment = '' where id = 2;
			select * from employee where post_comment = "";
			
		# (5) 关键字in集合查询
			#查询收入是3千或者3千5或者4千或者9千所有员工姓名,收入
			# 普通版
			select emp_name,salary from employee where salary=3000 or salary=4000 or salary=9000 or salary=3500;
			# 优化版
			select emp_name,salary from employee where salary in (3000,4000,3500,9000);
			# 取反
			select emp_name,salary from employee where salary not  in (3000,4000,3500,9000);
			
		# (6) 关键字like的模糊查询
			#(1) 通配符 %
			select * from employee where emp_name like "eg%";
			#(2) 通配符"_"
			select * from employee where emp_name like "al__";
		# (7) sql 函数concat(参数1,参数2,参数3) 把所有参数拼接在一起
			select emp_name,concat("姓名:",emp_name," 薪水: ",salary) from  employee;
			# as 就是起别名 不加as也可以;
			select emp_name,concat("姓名:",emp_name," 薪水: ",salary) as cs  from  employee;
			select emp_name,concat("姓名:",emp_name," 薪水: ",salary) cs  from  employee;
	# 完整格式 select * from 表 where 条件表达式
								group by
								having
								order by
								limit
	# 二.group by 分组: 有几个种类就有几个数据
		"""
		group by + 字段  所谓分组就是分类 
		后面的字段 一般会写在select 查询的后面;
		group_concat() 对分组的内容进行拼接;
		"""
		select depart_id from employee  group by depart_id;
		select depart_id from employee  group by post; # group by 后面接的是哪个字段,就搜这个字段,否则报错;
		select group_concat(emp_name),post from employee group by post
		
		# 聚合函数:
			# count(*) : 统计总数
			select count(*) from employee;
			# 统计最大值max
			select max(salary)  from employee;
			# 统计最小值min
			select min(salary)  from employee;
			# 统计平均值avg
			select avg(salary)  from employee;
			# 统计总和sum
			select sum(salary)  from employee;
			
		# 分组+聚合函数
			# 求各部门的平均薪资
			select avg(salary),post  from employee group by post
			# 求各部门的薪资最大值
			select max(salary),post  from employee group by post
		
	# 三.having 查完数据后再过滤:配合group by使用,主要用于分组之后的在过滤
		# 比如: 求部门的平均薪资,在10000以上的部门
		select avg(salary),post  from employee group by post having avg(salary) > 10000;
		# 1.查询各岗位内包含的员工个数小于2的    岗位名、员工名、个数拼在一起
		select post,group_concat(emp_name),count(*) from employee  group by post having count(*) < 2;
		
		# 2.查询各岗位平均薪资大于10000的岗位名、平均工资
		# 3.查询各岗位平均薪资大于10000且小于20000的岗位名、平均工资
		
	# 四.order by 按照什么字段排序
		# 默认升序 asc 从小到大排序
		select emp_name , age from employee where post = "teacher" order by emp_name;
		# 倒序  desc 从大到小排序
		select emp_name , age from employee where post = "teacher" order by age desc;
		# 1. 查询所有员工信息，先按照age升序排序，如果age相同则按照hire_date降序排序
		select * from employee order by age,hire_date desc;
		# 2. 查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资升序排列
		# 3. 查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资降序排列

	# 五.limit 限制查询的次数;[用来做数据分页的]
		limit(m,n) 默认m是0代表第一条数据,n所代表的时查询几条,从m+1条数据开始查询,查询n条
		# 1.查询最后一条数据
		select * from employee order by id desc limit 1;
		
		# 2.limit(m,n) 默认m的值是0 代表第一条数据,n所代表的是查询几条,从的m+1条数据开始,查询n条数据;
		select * from employee limit 0,5  # 0代表的是第一条数据,不是id
		select * from employee limit 5,5  # 5代表的是第六条数据,不是id 
# ### 2.多表间的查询
	# (1) 内联 (inner join ) : 两表或者多表进行查询 :两表或者多表中的数据或者条件都满足,才能查到
		语法:select 字段 from 表1 inner join 表2 on 条件
		多表:select 字段 from 表1 inner join 表2 on 条件 inner join 表3 on 条件 inner join 表4 on 条件....
		
		# 联表查询 相当于 内联查询
		select * from employee,department where employee.dep_id  =  department.id;
		# 内联查询
		select * from employee  inner join department on  employee.dep_id = department.id
		# 用as起别名 as可以省略
		select * from employee as e  inner join department as  d on  e.dep_id = d.id;
		
	
	# (2) 外联
		(1) 左连接 (left join) : 以左表为主,右表为辅,完整查询左表数据,右表对不上的补null
			select * from employee emp left join  department dep on emp.dep_id = dep.id
		(2) 右连接 (right join): 以右表为主,左表为辅,完整查询右表数据,左表对不上的补null
			select * from employee emp right join  department dep on emp.dep_id = dep.id
		(3) 全连接 (union)     : 把所有数据形成并集
			select * from employee emp left join  department dep on emp.dep_id = dep.id
			union
			select * from employee emp right join  department dep on emp.dep_id = dep.id
	
		# 找出年龄大于25岁的员工和员工所在的部门:
		# 以内联的方式查询 employee 和 department 表数据,并且按照age字段倒序;
		
# ### 3.子查询
	"""
		1.子查询是将一个查询语句嵌套在另一个查询语句之中,用括号抱起来,表达一个整体
		2.一般用在from 和 where 或者 select查询的后面
		3.内存sql语句可以作为外层sql语句的条件,也可以是表或字段;
		4.速度从块->慢   单条语句查询 >  联表查询 > 子查询
		5.子查询可以使用where所有符号 加上一个exists关键字...
	"""
	# (1) 找出平均年龄大于25岁以上的部门;
		# 单纯的查出来了 部门id  少他的名字
		select dep_id from employee  group by dep_id  having  avg(age) > 25;
		# 升级 group by 后面接什么字典 ,select 就查什么字段,其他的不行,除非是聚合函数;
		select department.name 
		from employee inner join department on employee.dep_id = department.id  
		group by department.name  
		having  avg(age) > 25;
		
		# 子查询
		select name from department
		where id in (200,201)
		
		# 升级
		(select dep_id from employee group by dep_id having avg(age) > 25) 查出所有满足条件的id
		
		select name from department
		where id in (select dep_id from employee group by dep_id having avg(age) > 25)	
		
		
		
	# (2) 查看技术部门所有员工姓名;
		# 联表查询
		select e.name  from employee as e , department as d  where e.dep_id = d.id and  d.name = "技术";
		# 内联查询
		select e.name 
		from  employee as e inner join department as d 
		on  e.dep_id = d.id
		where  d.name = "技术"
		# 子查询
		(1)select id  from department where name = "技术"
		(2)select name from employee where dep_id = ?
		(3)select name from employee where dep_id = (select id  from department where name = "技术") 
		
	# (3) 查看哪个部门没员工?
	# (4) 查询大于平均年龄的员工名与年龄
	# (5) 把大于其本部门平均年龄的员工名和姓名查出来
	# (6) 查询每个部门最新入职的那位员工 
	
	# (7) 带EXISTS关键字的子查询
	"""
	exists 关键字表示存在
		如果内层sql能够查询数据,返回True ,外层sql执行查询数据
		如果内存sql不能查询数据,返回False,外层sql不执行查询操作
	"""
	select * from employee
	where exists
	(select * from department where id = 200)















