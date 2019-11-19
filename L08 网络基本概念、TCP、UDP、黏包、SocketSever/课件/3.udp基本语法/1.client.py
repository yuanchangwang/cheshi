import socket
sk = socket.socket(type=socket.SOCK_DGRAM)

# sendto (要发送的消息, (ip地址,端口号))
sk.sendto("你好呀".encode("utf-8") ,("127.0.0.1",9000)  )

# 关闭udp连接
sk.close()
