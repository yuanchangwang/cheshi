import socket
import time 

sk = socket.socket()
sk.bind( ("127.0.0.1" , 9000) )
sk.listen()


conn,addr = sk.accept()
# 收发数据的逻辑
# ...
conn.send("00000120".encode("utf-8"))
msg = "hello," * 20
conn.send(msg.encode("utf-8"))

conn.send("world".encode("utf-8"))


# 四次挥手
conn.close()
# 退回端口
sk.close()

'''
使用8个字节进行固定发送的时,可以解决平常大多数问题
但是没有从根本解决所有数据能都发送接收的情况.
长度上还是受限制.
'''


