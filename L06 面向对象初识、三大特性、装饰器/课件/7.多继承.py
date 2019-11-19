# ### 多继承
class Father():
	f_property = "一朵梨花压海棠"
	def f_hobby(self):
		print("说学逗唱,吃喝嫖赌")
		
class Mother():
	m_property = "一枝红杏出墙来"
	def m_hobby(self):
		print("做饭,擦地,洗衣服,拖地板,买菜,看孩子")

# 女儿继承了父亲和母亲两个父类,两个父类的公有属性方法都可以被子类使用.
class Daughtor(Father,Mother):	
	pass
	
obj = Daughtor()	
print(obj.f_property)
obj.m_hobby()

# ### super 调用父类的相关公有属性方法
'''
(1)super本身是一个类 super()是一个对象 用于调用父类的绑定方法
(2)super() 只应用在绑定方法中,默认自动传递self对象 (前提:super所在作用域存在self)
(3)super用途: 解决复杂的多继承调用顺序	
'''
print("<=====>")
class Father():
	f_property = "一朵梨花压海棠"
	def f_hobby(self):
		print("说学逗唱,吃喝嫖赌")
	
	# def m_hobby(self):
		# print("做饭,擦地,洗衣服,拖地板,买菜,看孩子111")
		
class Mother():
	m_property = "一枝红杏出墙来"
	def m_hobby(self):
		print("做饭,擦地,洗衣服,拖地板,买菜,看孩子222")
		
class Son(Father,Mother):
	f_property = 123
	# 调用属性方法时,如果子类有,拿子类自己的,如果子类没有,拿父类的.
	def s_skill1(self):
		# 调用父类的公有属性方法
		print(self.f_property)
		self.m_hobby()
		print('<==>')
		# 类去调用成员属性
		print(Father.f_property)
		# 类去调用成员方法
		Mother.m_hobby(123) # 形参实参一一对应
		
		
	def s_skill2(self):
		# 一定调用父类的属性方法
		res = super().f_property
		print(res)
		
		super().m_hobby()
# 实例化对象 , 类的实例化
obj = Son()
obj.s_skill1()
# obj.s_skill2()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		