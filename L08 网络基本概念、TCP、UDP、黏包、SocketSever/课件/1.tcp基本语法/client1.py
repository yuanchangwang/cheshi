# ### 客户端

import socket
# 产生一个socket对象
sk = socket.socket()
# 建立连接
sk.connect( ("127.0.0.1",9000) )

# send 发送消息 参数必须是二进制的字节流
sk.send("早".encode("utf-8"))

# recv 接收消息
res = sk.recv(1024)
print(res.decode("utf-8"))
# 关闭连接
sk.close()



