### os模块-对系统进行操作

```
#system()  在python中执行系统命令
#popen()   执行系统命令返回对象,通过read方法读出字符串
#listdir() 获取指定文件夹中所有内容的名称列表
#getcwd()  获取当前文件所在的默认路径
#chdir()   修改当前文件工作的默认路径
#environ   获取或修改环境变量
#--os 模块属性
#name 获取系统标识   linux,mac ->posix      windows -> nt
#sep 获取路径分割符号  linux,mac -> /       window-> \
#linesep 获取系统的换行符号  linux,mac -> \n    window->\r\n 或 \n
```

### os路径模块 -os.path

```
#abspath()  将相对路径转化为绝对路径
#basename() 返回文件名部分
#dirname()  返回路径部分
#split() 将路径拆分成单独的文件部分和路径部分 组合成一个元组
#join()  将多个路径和文件组成新的路径 可以自动通过不同的系统加不同的斜杠  linux / windows\
#splitext() 将路径分割为后缀和其他部分
#getsize()  获取文件的大小
#isdir()    检测路径是否是一个文件夹
#isfile()   检测路径是否是一个文件
#islink()   检测路径是否是一个链接
#getctime() [windows]文件的创建时间,[linux]权限的改动时间(返回时间戳)
#getmtime() 获取文件最后一次修改时间(返回时间戳)
#getatime() 获取文件最后一次访问时间(返回时间戳)
#exists()   检测指定的路径是否存在
#isabs()    检测一个路径是否是绝对路径
```

### os 与 shutil 模块 都具备对文件的操作

```
# -- os模块具有 新建/删除/
#os.mknod   创建文件
#os.remove  删除文件
#os.mkdir   创建目录(文件夹)
#os.rmdir   删除目录(文件夹)
#os.rename  对文件,目录重命名
#os.makedirs   递归创建文件夹
#os.removedirs 递归删除文件夹（空文件夹）
```

### shutil模块

```
# -- shutil模块 复制/移动/
#copyfileobj(fsrc, fdst[, length=16*1024])  复制文件 (length的单位是字符(表达一次读多少字符))
#copyfile(src,dst)   #单纯的仅复制文件内容 , 底层调用了 copyfileobj
#copymode(src,dst)   #单纯的仅复制文件权限 , 不包括内容  (虚拟机共享目录都是默认777)
#copystat(src,dst)   #复制所有状态信息,包括权限，组，用户，修改时间等,不包括内容
#copy(src,dst)       #复制文件权限和内容
#copy2(src,dst)      #复制文件权限和内容,还包括权限，组，用户，时间等
#copytree(src,dst)   #拷贝文件夹里所有内容(递归拷贝)
#rmtree(path)        #删除当前文件夹及其中所有内容(递归删除)
#move(path1,paht2)   #移动文件或者文件夹
```
### json模块

```
# 所有编程语言都能够识别的数据格式叫做json,是字符串
#dumps 把任意对象序列化成一个str
#loads 把任意str反序列化成原来数据
#dump  把对象序列化后写入到file-like Object(即文件对象)
#load  把file-like Object(即文件对象)中的内容拿出来,反序列化成原来数据

# json 和 pickle 两个模块的区别:
(1)json序列化之后的数据类型是str,所有编程语言都识别,
   但是仅限于(int float bool)(str list tuple dict None)
   json不能连续load,只能一次性拿出所有数据
(2)pickle序列化之后的数据类型是bytes,
   所有数据类型都可转化,但仅限于python之间的存储传输.
   pickle可以连续load,多套数据放到同一个文件中
```

### 压缩模块-zipfile (后缀为zip)

```
#zipfile.ZipFile(file[, mode[, compression[, allowZip64]]])
#ZipFile(路径包名,模式,压缩or打包,可选allowZip64)
#功能：创建一个ZipFile对象,表示一个zip文件.
#参数：
    -参数file表示文件的路径或类文件对象(file-like object)
    -参数mode指示打开zip文件的模式，默认值为r
        r    表示读取已经存在的zip文件
        w    表示新建一个zip文档或覆盖一个已经存在的zip文档
        a    表示将数据追加到一个现存的zip文档中。
    -参数compression表示在写zip文档时使用的压缩方法
        zipfile.ZIP_STORED      只是存储模式，不会对文件进行压缩，这个是默认值
        zipfile.ZIP_DEFLATED    对文件进行压缩 
    -如果要操作的zip文件大小超过2G，应该将allowZip64设置为True。

#压缩文件
#1.ZipFile()          写模式w打开或者新建压缩文件
#2.write(路径,别名)   向压缩文件中添加文件内容
#3.close()            关闭压缩文件

#解压文件
#1.ZipFile()             读模式r打开压缩文件
#2.extractall(路径)      解压所有文件到某个路径下
#  extract(文件,路径)    解压指定的某个文件到某个路径下
#3.close()               关闭压缩文件

#追加文件(支持with写法)
ZipFile()                追加模式a打开压缩文件

#查看压缩包中的内容
namelist()
```

### 压缩模块-tarfile(后缀为.tar  |  .tar.gz  |   .tar.bz2)  (了解)

```
#bz2模式的压缩文件较小  根据电脑的不同会差生不同的结果 (理论上:bz2压缩之后更小,按实际情况为标准)

w     单纯的套一个后缀 打包
w:bz2 采用bz2算法 压缩    
w:gz  采用gz算法 压缩

#压缩文件
#1.open('路径包名','模式','字符编码') 创建或者打开文件 
#2.add(路径文件,arcname="别名") 向压缩文件中添加文件
#3,close() 关闭文件

#解压文件
#1.open('路径包名','模式','字符编码') 读模式打开文件 
#2.extractall(路径)      解压所有文件到某个路径下
#  extract(文件,路径)    解压指定的某个文件到某个路径下
#3.close()               关闭压缩文件

#追加文件
open()                   追加模式 a: 打开压缩文件 正常添加即可

#查看压缩包中的内容
getnames()    
```