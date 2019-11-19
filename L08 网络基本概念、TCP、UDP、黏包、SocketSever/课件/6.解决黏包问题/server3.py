import socket
import time 
import struct

sk = socket.socket()
sk.bind( ("127.0.0.1" , 9000) )
sk.listen()


conn,addr = sk.accept()
# 收发数据的逻辑
# ...

inp = input(">>>msg:")
msg = inp.encode("utf-8")
# pack 方法 算出的值已经是4个字节长度二进制字节流
res = struct.pack("i",len(msg))

conn.send(res)
conn.send(msg)

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


