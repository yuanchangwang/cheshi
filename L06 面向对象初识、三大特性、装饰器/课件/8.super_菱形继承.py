# ### 菱形继承 
'''
   Human

Man      Woman
	
  Children
'''
class Human():
	pty = 111
	def feelT(self):
		print("远古人类,天冷了,生火烤火1")
		print(self.pty)
		print("远古人类,天热了,跳海喂鱼2")


class Man(Human):
	pty = 222
	def feelT(self):
		print("男人天冷了, 喝二锅头 , 暖暖身体, 消消毒3")
		super().feelT()
		print("男人天热了, 吃冰淇淋4")

class Woman(Human):
	pty = 333
	def feelT(self):
		print("女人天冷了,买衣服,买买买5")
		super().feelT()
		print("女人天热了,光膀子,买买买6")

class Children(Man,Woman):
	pty = 444
	def feelT(self):
		print("小孩天冷了,就哭7")
		super().feelT()
		print("小孩天热了,还是哭8")
		
obj = Children()
obj.feelT()		
'''	
# mro列表  类.mro() 使用c3算法,针对于多继承的情况,按照这个列表依次调用.调用顺序都在其中
# 如果出现重名方法,  super() 就是按照这个列表依次调用
'''
res = Children.mro()
print(res)
'''
[
<class '__main__.Children'>, 
<class '__main__.Man'>, 
<class '__main__.Woman'>, 
<class '__main__.Human'>,
 <class 'object'>
 ]
'''
# 7351  2648
		
		
# 判断子父关系issubclass
# 判断类型 isinstance
res= issubclass(Children,Man)
# 判断Children 是不是元组当中一个类的子类,有一个成立,返回真,一个都不满足,返回假
res = issubclass(Children,(Man,Woman))
# 只要有血缘关系即可.
res = issubclass(Children,Human)
print(res)


# 判断obj这个对象类型是不是Children (有继承的血缘关系即可)
'''
python当中,万物皆是对象,只是对象常常这两字被省略.
'''
res = isinstance(obj,Children)
res = isinstance(obj,Human)
res = isinstance(obj,(Man,Woman))
print(res)














		
		
		
		
		
		
		
		