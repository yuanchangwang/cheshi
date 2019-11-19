# ### 多态
'''
不同的子类对象,调用相同的父类方法,产生不同的执行结果
(1) 继承  (2)重写
在不改变原有代码的前提下,实现了不同的效果
'''

class Soldier():
	# 攻击
	def attack(self):
		pass
	# 后退
	def back(self):
		pass

# 陆军
class Army(Soldier):
	def attack(self):
		print("[陆军]以迅雷不及掩耳之势,夺得敌军的高地")
		
	def back(self):
		print("[陆军]保命要紧,撒腿就跑")
	
# 海军
class Navy(Soldier):
	def attack(self):
		print("[海军]在海底发射鱼雷,击毁敌方的军舰")

	def back(self):
		print("[海军]深入海底,跳海喂鱼")

# 空军
class AirForce(Soldier):
	def attack(self):
		print("[空军]发射它的意大利炮,把二营长的意大利炮端上来")
	def back(self):
		print("[空军]弃机跳伞,落地成盒")

# 类的实例化 返回陆军对象
army_obj = Army()
# 类的实例化 返回海军对象
navy_obj = Navy()
# 类的实例化 返回空军对象
af_obj = AirForce()

# 各就位准备
listvar = [army_obj,navy_obj,af_obj]


# 将军下达命令
sign = True
while sign:
	strvar = """
	1.全体攻击
	2.全体撤退
	3.空军上,其他人撤退
	"""
	print(strvar)
	num = input("将军,请下达您的指令:")
	
	
	if num == "1":
		for i in listvar:
			i.attack()
			
	elif num == "2":
		for i in listvar:
			i.back()
			
	elif num == "3":
		for i in listvar:
			# 如果当前的对象是空军类型的,调用attack方法
			if isinstance(i,AirForce):
				i.attack()
			# 否则调用back方法
			else:
				i.back()
				
	elif num.upper() == "Q":
		# sign=False
		break
				
	else:
		print("报告长官,风太大,我听不到")
		






















