# 服务器
import socket
import time
sk = socket.socket()
# 注册主机到网络
sk.bind( ("127.0.0.1",9000) )
sk.listen()

# 三次握手
conn,addr = sk.accept()

# 收发数据的逻辑
# ...
conn.send("hello,".encode("utf-8"))

conn.send("world".encode("utf-8"))


# 四次挥手
conn.close()
# 退回端口
sk.close()




