# ### 计算一个文件夹当中所有文件的大小
import os
pathvar = "D:\深圳周末三期\L006\lianxi_abc"
lst = os.listdir(pathvar)
print(lst)


# (1)计算文件大小
size = 0
for i in lst:
	# print(i)
	#"D:\深圳周末三期\L006\lianxi_abc"  + a.txt => 通过join 拼接新的路径
	#  "D:\深圳周末三期\L006\lianxi_abc\a.txt"
	# 拼接路径  用来判断是文件夹还是问价
	pathvar2 = os.path.join(pathvar,i)
	# 如果是文件夹 执行相应逻辑
	if os.path.isdir(pathvar2):
		print(i+"是[目录]")
	# 如果是文件, 计算文件大小
	elif os.path.isfile(pathvar2):
		print(i+"是[文件]")
		# os.path.getsize 只能计算文件的大小
		# 用size 这个变量不停的累加文件大小
		size += os.path.getsize(pathvar2)
		
print(size)
	
# 742 + 272 = 1014  + 4334 = 5348


#(2) 使用递归来计算文件的总大小
pathvar = "D:\深圳周末三期\L006\lianxi_abc"
def getallsize(pathvar):
	size = 0
	lst = os.listdir(pathvar)
	print(lst) #['a.txt', 'b.txt', 'ceshi333']
	'''
	#pathvar2 = os.path.join(pathvar,i)
		D:\深圳周末三期\L006\lianxi_abc\a.txt
		D:\深圳周末三期\L006\lianxi_abc\b.txt
		D:\深圳周末三期\L006\lianxi_abc\ceshi333
	'''
	for i in lst:
		pathvar2 = os.path.join(pathvar,i)
		if os.path.isdir(pathvar2):
			# 模拟鼠标点击进去的动作
			'''size += getallsize(pathvar2) 是和上一个代码唯一不一样的地方;'''		
			size += getallsize(pathvar2)
		
			print("是文件夹")
		elif os.path.isfile(pathvar2):
			size += os.path.getsize(pathvar2)
	return size
res = getallsize(pathvar)
print(res)
# D:\深圳周末三期\L006\lianxi_abc\ceshi333






























