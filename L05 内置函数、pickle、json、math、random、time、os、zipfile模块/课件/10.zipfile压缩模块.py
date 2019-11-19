# ### zipfile  文件压缩
import zipfile
# zipfile.ZIP_DEFLATED 对当前文件进行压缩
# 1.压缩文件
# (1)创建一个压缩文件
zf = zipfile.ZipFile("ceshi0512.zip","w",zipfile.ZIP_DEFLATED)
# (2)往压缩包当中存入内容 推荐写入绝对路径
# (路径参数,别名参数)
zf.write(r"D:\深圳周末三期\L006\2.pickle.py","2.pickle.py")
zf.write(r"D:\深圳周末三期\L006\3.json.py","3.json.py")

# (3)关闭文件
zf.close()

# 2.解压文件
zf = zipfile.ZipFile("ceshi0512.zip","r")
# (1)extractall(路径)      解压所有文件到某个路径下
# zf.extractall("D:\深圳周末三期\L006\ceshi0512")

# (2)extract(文件,路径)    解压指定的某个文件到某个路径下
zf.extract("2.pickle.py","D:\深圳周末三期\L006\ceshi0512\dange")
zf.close()


# (3)追加文件(支持with写法)
with zipfile.ZipFile("ceshi0512.zip","a",zipfile.ZIP_DEFLATED) as zf:
	# 可以在write写入的时候 , 临时创建文件夹 比如 tmp/555666 这个tmp就是临时文件夹
	zf.write(r"D:\深圳周末三期\L006\4.math.py","tmp909090/5555666")

# (4)查看压缩包中的内容
with zipfile.ZipFile("ceshi0512.zip","r") as zf:
	res = zf.namelist()
print(res) #['2.pickle.py', '3.json.py', 'tmp909090/5555666']
