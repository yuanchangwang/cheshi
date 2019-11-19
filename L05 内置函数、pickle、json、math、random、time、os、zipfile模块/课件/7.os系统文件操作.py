# ### os模块 对系统进行操作
import os
# os.system("ipconfig")
# os.system('calc')
# os.system("mspaint")

# popen 可以把运行的结果,这个字符串转化成utf-8这样的编码格式在进行输出
res = os.popen("ipconfig").read()
print(res)

#listdir() 获取指定文件夹中所有内容的名称列表
lst = os.listdir(r"D:\深圳周末三期\L006") 
print(lst)
'''
['0512.txt', 
'0512_1.txt', 
'0512_2.txt', 
'0512_3.txt', 
'0512_4.txt', 
'1.内置函数.py',
 '2.pickle.py',
 '20190512_上午_模块json_pickle_math_内置.mp4', '3.json.py', 
 '4.math.py', '5.random.py', '6.time.py', '7.py', 'part10.md',
 'part11.md', 'part6.md']
'''

#getcwd()  获取当前文件所在的默认路径
res = os.getcwd()  #D:\深圳周末三期\L006
print(res)


#chdir()   修改当前文件工作的默认路径
os.chdir("D:\深圳周末三期\L006\lianxi_abc")
#os.mkdir   创建目录(文件夹)
# os.mkdir("ceshi_111")
#os.rmdir   删除目录(文件夹)
# os.rmdir("ceshi_111")
#os.rename  对文件,目录重命名
# os.rename("ceshi_222","ceshi333")
#copy(src,dst)       #复制文件权限和内容
import shutil
# . 当前路径 .. 代表上一级路径 ../../c.txt 代表上一级的上一级
# 把当前路径的a.txt 复制到 上一级的b.txt文件中
shutil.copy("a.txt","../b.txt")

#environ   获取或修改环境变量  
res = os.environ
print(res)
# os.system("QQScLauncher.exe")
'''
需求:通过pycharm 能够执行qq程序:
(1)需要能够找到实际的路径在进行执行,找不到路径执行不了
环境变量当中,有一个专门用来存储路径的键,叫做PATH环境变量
当调用一个程序的时,先去os.environ['PATH'] 寻找路径,
如果找到了,直接通过该路径执行程序,
如果找不到,直接报错,不是内部命令.
'''




"""

res = os.environ['PATH']  #
# print(res,type(res))    # 获取PATH这个环境变量里面的内容
os.environ['PATH'] += "D:\Program Files (x86)\Tencent\QQ\Bin;" # 在PATH当中添加路径
# 以便于执行qq的时候,能找到实际的程序.
os.system('QQScLauncher.exe')
"""




r'''
#D:\pycharm_lianxi\venv\Scripts;
C:\Python36\Scripts\;
C:\Python36\;
C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\iCLS\;
C:\Program Files\Intel\Intel(R) Management Engine Components\iCLS\;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;C:\Users\KnightPlan\AppData\Local\Microsoft\WindowsApps;;C:\Program Files\JetBrains\PyCharm 2018.3.5\bin;
'''

'''
environ(
{'ALLUSERSPROFILE': 'C:\\ProgramData', 
'APPDATA': 'C:\\Users\\KnightPlan\\AppData\\Roaming',
 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 
 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files',
 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files',
 'COMPUTERNAME': 'DESKTOP-CESIAF0', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\KnightPlan', 'LOCALAPPDATA': 'C:\\Users\\KnightPlan\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-CESIAF0', 'NUMBER_OF_PROCESSORS': '6', 'OS': 'Windows_NT', 'PATH': 'D:\\pycharm_lianxi\\venv\\Scripts;C:\\Python36\\Scripts\\;C:\\Python36\\;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\iCLS\\;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\iCLS\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Users\\KnightPlan\\AppData\\Local\\Microsoft\\WindowsApps;;C:\\Program Files\\JetBrains\\PyCharm 2018.3.5\\bin;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 158 Stepping 10, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '9e0a', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PROMPT': '(venv) $P$G', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PT7HOME': 'd:\\Program Files\\Cisco Packet Tracer 7.1.1', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM': 'C:\\Program Files\\JetBrains\\PyCharm 2018.3.5\\bin;', 'PYCHARM_HOSTED': '1', 'PYCHARM_MATPLOTLIB_PORT': '60112', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'D:\\pycharm_lianxi;C:\\Program Files\\JetBrains\\PyCharm 2018.3.5\\helpers\\pycharm_matplotlib_backend', 'PYTHONUNBUFFERED': '1', 'QT_DEVICE_PIXEL_RATIO': 'auto', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\KNIGHT~1\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\KNIGHT~1\\AppData\\Local\\Temp', 'USERDOMAIN': 'DESKTOP-CESIAF0', 'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-CESIAF0', 'USERNAME': 'KnightPlan', 'USERPROFILE': 'C:\\Users\\KnightPlan', 'VIRTUAL_ENV': 'D:\\pycharm_lianxi\\venv', 'WINDIR': 'C:\\Windows', '_OLD_VIRTUAL_PATH': 'C:\\Python36\\Scripts\\;C:\\Python36\\;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\iCLS\\;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\iCLS\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Users\\KnightPlan\\AppData\\Local\\Microsoft\\WindowsApps;;C:\\Program Files\\JetBrains\\PyCharm 2018.3.5\\bin;', '_OLD_VIRTUAL_PROMPT': '$P$G'})
'''


#--os 模块属性
#name 获取系统标识   linux,mac ->posix      windows -> nt
print(os.name)
#sep 获取路径分割符号  linux,mac -> /       window-> \  *****
print(os.sep)  # /home/wangwen/abc  \home\wangwen #error
#linesep 获取系统的换行符号  linux,mac -> \n    window->\r\n 或 \n
print(repr(os.linesep))








