# 客户端
import socket
import time
import struct
sk = socket.socket()
sk.connect( ("127.0.0.1",9000) )


time.sleep(0.1)

# n = int(sk.recv(8).decode("utf-8"))

n = sk.recv(4)
# 获取元组当中的第一个值 , 因为他返回的是元组.
n = struct.unpack("i",n)[0]

# 收发数据的逻辑
print(sk.recv(n))


print(sk.recv(10))




sk.close()

