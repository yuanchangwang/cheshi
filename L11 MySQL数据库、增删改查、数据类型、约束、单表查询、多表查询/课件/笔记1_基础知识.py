# windows (在超级管理员的权限下执行)
net start mysql 启动mysql 
net stop mysql  停止mysql

# ### 1
# 数据库: 关系型数据库 , 菲关系数据库
关系型数据库 - mysql  oracle, sql servre
(把数据库存储在有行有列的二维表中这样的数据结构,如果是海量数据,mysql读写性能并不高,支持复杂的sql查询,和事务处理)

非关系型数据库 redis mongodb 
(以键值对这样的数据形式进行存储,没有固定的表结构,海量数据读写性能比较高,但复杂的sql查询或者事务处理欠缺)

# 存储引擎 (数据的存储方式)
# show engines 查看所有存储引擎 
	innodb : 5.6之后默认的存储引擎
	特点:支持事务,行级锁,外键
	
	myisam : 5.6之前默认的存储引擎
	特点: 表级锁

# 概念:
	事务:
		操作一些列sql语句,只有都实行成功才算成功
		有一个不成功,就恢复到初始状态,这个完整过程就是事务
		
	表级锁:
		有一个人修改了数据表,就会上锁,其他人不能修改
		特点:内存开销小,不支持并发
		
	行级锁:
		有一个人修改了数据表中的一条记录,这条记录,这条数据就会上锁,其他人不能改
		特点:内存开销大,支持并发

	外键:
		把多张表通过一个字段关联在一起,就是外键

# ### 2
# mysql 客户端 登录 mysql 服务端
# (1)登录
mysql -u 指定用户名 -p 指定密码 -h指定ip主机地址 默认值是localhost => 127.0.0.1
mysql -uroot -p
# 退出 exit  \q

# (2) 连接远程数据库
mysql -uroot -p -h 114.96.145.33
# 打开远程连接数据库当中的服务权限
grant 权限 on 数据库.表 to "用户名"@"ip地址" identified by "密码";
"""
all privileges 表示所有权限 (可以简写all)
select 查询数据库权限
insert 插入数据库权限
update 更新数据库权限
delete 删除数据库权限
"""
* 代表所有
grant all on *.* to "root"@"%" identified by "123456";
# 刷新权限,立刻生效
flush privileges;


# mysql 设置密码
# 查询当前登录的用户是谁
select user();
# 设置
set password = password("123456");
# 去除
set password = password('');


# ### 3
# 关于数据库的增删改查
sql 语句
操作数据库(文件夹)
	增:
		# 创建数据库db1,设置字符集utf8
		create database db1 charset utf8;
	查:
		#查看建库信息
		show create database db1;
		#显示所有数据
		show databases;	
	改:
		# 更改数据库字符集
		alter database db1 charset gbk;
	删:
		# 删除数据库db1
		drop database db1;
	
操作表(文件)
	int 整型 char varchar 字符串 enum 枚举类型(把可能的选项放进去)
	#如果想要使用这个数据库
	use 数据库名称
	use db1
	
	增:
		# 创建数据表
		create table t4(
		id int,
		name char
		);
		
	查:
		# 查看所有表
		show tables;
		# 查看建表语句
		show create table t4;
		show create table t4\G 查看时,以垂直分布显示;
		'''
		 CREATE TABLE `t4` (
		  `id` int(11) DEFAULT NULL,
		  `name` char(1) DEFAULT NULL
		) ENGINE=InnoDB DEFAULT CHARSET=utf8
		'''
		# 查看表结构
		desc t4;
	改:
		# modify 单纯该表数据类型 指定char的字符长度是6;
		alter table t4 modify name char(6);
		# change 连明带数据类型一起都改变.
		alter table t4 change name name123 char(7);
		# add  添加字段,enum是枚举类型
		alter table t4 add sex enum("man","woman");
		# drop 删除字段 drop column 删除列
		alter table t4 drop column name123;
		# 更改表名
		alter table t4 rename t1;	
		
	删:
		# 删除表t1
		drop table t1;
	
操作记录:(文件内容)
	增:
		# insert 插入 t2后面指定字段名称, values后面指定插入的数据 ,单条插入
		insert into t2(id,name) values(1,"xboy1");
		# 一次插入多条数据
		insert into t2(id,name) values(2,"xboy2"),(3,"xboy3"),(4,"xboy4");
		# 可以不指定具体字段,但是字段值需要一一对应
		insert into t2 values(5,"xboy5");
		# 可以指定具体某个字段插入值
		insert into t2(id) values(6)
		
	查:
		# 查询当前所使用的数据库是什么
		select database();
		#从t2这个表当中查询所有数据 * 代表所有字段
		select * from t2 ;
		# 库.表名
		select * from db1.t2;
	改:
		# update 表名 set 字段=值 where 条件
		update t2 set name = '王文222' 
		update t2 set name = '王文' where id = 6
		
	删:
		# 删除t2所有数据
		delete from t2;
		delete from t2 where id = 1;
		# 重置数据表(重置id)
		truncate table t2;


# ### 4 
# mysql 数据类型
# 整型:
tinyint: 1个字节 有符号(-128~127) 无符号unsigned(0~255)  小整数值
int:     4个字节 有符号(-21亿~ 21亿,最大长度10位) 无符号unsigned(0~42亿) 大整数值,精确度高

	create table t1(id int unsigned,sex tinyint);
	insert into t1 values(42000000,127);
	# insert into t1 values(4200000000000,3) error

# 浮点型:
float(255,30)  单精度 (推荐)
double(255,30) 双精度
decimal(65,30) 金钱类型
	create table t2(f1 float(5,2),f2 double(5,2),f3 decimal(5,2));
	insert into t2 values(1.234,1.234,1.234)

	# 在不指定数据长度的情况下,double小数位保留的长度更长,float默认保留5位小数,decimal默认四舍五入
	create table t3(f1 float,f2 double,f3 decimal);
	insert into t3 values(1.935555555555555,1.935555555555555,1.935555555555555);
	
	# float(5,2) 小数位保留2位,整数位最多保留3位;
	create table t3_1(f1 float(5,2));
	insert into t3_1 values(123.3456789);

# 字符串:
char(11)      定长:固定开辟长度为11的内存空间 , 速度快(手机号,身份证号)
varchar(11)   变长:最大开辟长度为11的内存空间 , 速度稍慢 (文章评论,5~15字符之内)
text          应用于大文本数据,小说,文章,科幻

# 时间类型
date YYYY-MM-DD 年月日 (出生日期)
time HH:MM:SS   时分秒 (竞赛时间)
year YYYY       年份   (82的红酒拉菲,矿泉水)
datetime YYYY-MM-DD HH:MM:SS 年月日时分秒 (登录,注册所用的时间,下单)
	
	create table t5(d date , t time , y year ,dt datetime);
	insert into t5 values(now(),now(),now(),now());
	insert into t5 values("2020-1-1","23:23:23","2019","2099-1-1 22:22:22");

timestamp YYYYMMDDHHMMSS 自动更新时间戳,不需要你手动写入(修改数据,自动更新,可以获取最后一次修改时间)
	create table t6(dt datetime,ts timestamp);
	# timestamp 自动更新时间,不需要手动插入 null 相当于python中的None,代表空的意思;
	insert into t6 values(null,null);
	# 手动插入
	insert into t6 values(20191030121113,20191030121113);

# 枚举集合类型
enum 枚举 从一组数据当中选一个(一般用在性别上)
set  集合 从一组数据当中选多个,自动去重(兴趣,爱好)

create table t7(
	id int unsigned ,
	name varchar(15),
	money float(6,2),
	sex enum("man","woman"),
	hobby set("eat","drink","sleep","play","chou")
	);

# 正确
insert into t7(id,name,money,sex,hobby) values(1,"wangwen",9.123459,"man","eat,drink,sleep");
# 自动去重
insert into t7(id,name,money,sex,hobby) values(2,"徐欣欣",8.134,"woman","eat,eat,eat");

# ### 5
# 约束
unsigned: 无符号整型
not null: 不能为空
default : 设置默认值
unique  : 唯一约束,数据是唯一的不能重复
primary key   : 主键,唯一并且不能空,记录唯一的一条数据(用来辨别数据的唯一性)
auto_increment: 自增加1 ,一般针对于主键进行设置
foreign key   : 外键,把多张表通过一个字段关联在一起

#not null: 不能为空
create table t7_2(id int unsigned not null,name varchar(255));
# insert into t7_2(name) values("2"); error
insert into t7_2 values(6,"3");

# default : 设置默认值
create table t8(id int unsigned  not null,name varchar(255) default "王文");
insert into t8 values(2,null);
insert into t8(id) values(3);

# unique  : 唯一约束,数据是唯一的不能重复,可以为null,null可以插入多个
create table t9(id int unique ,name char(12) default "lisi");
insert into t9(id) values(1);
insert into t9(id) values(null);
insert into t9(id) values(null);

# primary key   : 主键,唯一并且不能空,记录唯一的一条数据(用来辨别数据的唯一性) 如果给一个字段设置主键,一个表中只能有一个.
create table t10(id int not null unique,name char(10) default "徐冬冬");
create table t11(id int  primary key,name char(10) default "龙阳");
# insert into t11 values(null); error

# not null unique 和 primary key 如果同时存在,优先primary key为主键,优先级最高.
create table t12(id int not null unique , name char(10) primary key);


# auto_increment: 自增加1 ,一般针对于主键进行设置
create table t13(id int primary key auto_increment , name char(10) default "123");
insert into t13(id) values(null);

# foreign key   : 外键,把多张表通过一个字段关联在一起
	"""外键要求:所关联的字段必须是唯一的 (要么unique ,要么主键,一般设主键为关联字段)"""
	student:
		id     name   age  classname
	     1   wangwen   18   python3
		 2   xudong    78   python3
		 3   dabao     99   python3
		 4   dasao     999  python3
	# 出现了过多冗余的数据,开始分表,利用外键关联
	student1:
		id   name       age    class_id
        1    wangwen    18        3
	    2   longyang    998       3
		3   xudong      9998      3
		4   chenchubing 99999     3

	class1:
		id  classname  time
		1   python5    1989-1-1
		2   python6    789-2-1
		3   python3    10-1-1
		
	# 先创建class1表  
	#  外键       字段       关联         id字段
	# ,foreign key(class_id) references class1(id)
	create table class1(id int , classname varchar(255));
	create table student1(id int primary key auto_increment,name varchar(255),age int ,class_id int,foreign key(class_id) references class1(id));
	# 设置id为unique 唯一索引,通过外键关联的字段必须是唯一
	alter table class1 add unique(id);
	# MUL 普通索引
	desc student1
	
	
	# 插入数据库
	insert into class1 values(1,"python5"),(2,"python6"),(3,"python7");
	insert into student1 values(null,"王文",18,1),(null,"徐冬冬",99,2),(null,"陈出兵",99999,3);
	
	# 如果形成了外键关系(本身表中有外键的可以删,有外键关联的另外一张表是不允许的)
	delete from class1 where id = 1; 不行
	delete from student1 where id = 1;可以
	只要有一条数据与class1有关联就不能删除
	insert into student1 values(null,"徐冬冬",99,2),(null,"陈出兵",99999,3);
	
	"""
	on update cascade  联级更新
	on delete cascade  联级删除
	"""
	create table class2(id int unique,classname varchar(255));
	create table student2(id int primary key auto_increment,name varchar(255),age int,class_id int,
	foreign key(class_id) references class2(id) on update cascade on delete cascade 	
	);
	如果要删除class2中的数据,那么连带这个外键所对应的值都删了.
	如果要更新class2中的数据,那么连带这个外键所对应的值都更新了.
	
	
	insert into class2 values(1,"python5"),(2,"python6"),(3,"python7");
	insert into student2 values(null,"王文",18,1),(null,"徐冬冬",99,2),(null,"陈出兵",99999,3);
	
	# 表与表之间的关系:
	(1) 一对一: 一个人一个身份证号
	(2)一对多或多对一:一个班级对应多个学习[在多的那个表里创建外键,关联另外一个表的字段]
	(3)多对多:一个学生对应多个学科,一个学科被多个学生学习,
	
	xueke (主表1)
	id  name
	1   math
	2   huaxue
	3   english
	4   wuli
	
	student:(主表2)
	id  name
	1   wangwen
	2   lisi
	3   zhangsan 
	
	relation (多对多,把xid 和 sid 设置成外键)
	xid  sid
	1     1
	1     2
	1     3
	2     1
	2     2
	2     3
	3     1
	3     2
	3     3
"""
# 总结:
1.添加/删除 not null约束
	alter table 表名 modify 别名 类型
	
2.添加/删除 unique 唯一索引
	alter table 表名 add unique(id);
	alter table 表名 drop index 索引名
	
3.添加/删除primary key 主键
	alter table 表名 add primary key(id)
	alter table 表名 drop primary key;
	
4.添加/删除foreign key 外键
	alter table student2 drop foreign key student2_ibfk_1
	alter table student2 add  foreign key(class_id) references class2(id)
"""

# ### 6
看笔记第二部分


# 数据库函数
# 获取当前时间
select now() 
now()  

































