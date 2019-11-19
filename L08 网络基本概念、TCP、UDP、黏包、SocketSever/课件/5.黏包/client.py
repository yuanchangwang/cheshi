# 客户端
import socket
import time
sk = socket.socket()
sk.connect( ("127.0.0.1",9000) )


# time.sleep(0.1)

# 收发数据的逻辑
print(sk.recv(10))


print(sk.recv(10))




sk.close()




