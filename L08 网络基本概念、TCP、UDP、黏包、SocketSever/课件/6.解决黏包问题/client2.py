# 客户端
import socket
import time
sk = socket.socket()
sk.connect( ("127.0.0.1",9000) )


time.sleep(0.1)

n = int(sk.recv(8).decode("utf-8"))

# 收发数据的逻辑
print(sk.recv(n))


print(sk.recv(10))




sk.close()




