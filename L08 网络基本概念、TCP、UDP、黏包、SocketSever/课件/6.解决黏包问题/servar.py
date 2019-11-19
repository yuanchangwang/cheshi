import socket
import time 

sk = socket.socket()
sk.bind( ("127.0.0.1" , 9000) )
sk.listen()


conn,addr = sk.accept()
# 收发数据的逻辑
# ...
conn.send("6".encode("utf-8"))
conn.send("hello,".encode("utf-8"))

conn.send("world".encode("utf-8"))


# 四次挥手
conn.close()
# 退回端口
sk.close()

'''
因为tcp 无边界的特征: 按照recv后面括号里面的值来进行接受数据
完全有可能在客户端 因为延迟问题,导致两次发送的数据黏在一起
因为tcp无边界,按照实际10个字节进行截图,根本分不清
是第几次发送的. 从而黏包.

解决的方式:
告诉客户端,直接你要截取的字节数是多少,
按照send发送的实际字节数,进行截取.
'''









