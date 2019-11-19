# ### math 数学模块
#ceil()  向上取整操作 (对比内置round)
import math
res = math.ceil(4.01)
print(res)

#floor() 向下取整操作 (对比内置round)
res = math.floor(3.99)
print(res)

#pow()  计算一个数值的N次方(结果为浮点数) (对比内置pow)
res = math.pow(2,3)
print(res)
# math模块中的pow没有第三个参数
# res = math.pow(2,3,3) error
# print(res)

#sqrt() 开平方运算(结果浮点数)
res = math.sqrt(10)
print(res)

#fabs() 计算一个数值的绝对值 (结果浮点数) (对比内置abs)
res = math.fabs(-56)
print(res)

#modf() 将一个数值拆分为整数和小数两部分组成元组
res = math.modf(14.677)
print(res)

#copysign()  将参数第二个数值的正负号拷贝给第一个
res = math.copysign(-1,-5)
print(res) # 得到浮点数结果 , 它的正负号取决于第二个值

#fsum() 将一个容器数据中的数据进行求和运算 (结果浮点数)(对比内置sum)
listvar = [1,2,3,4,5,99,6]
res = math.fsum(listvar)
print(res)

#圆周率常数 pi
print(math.pi)










