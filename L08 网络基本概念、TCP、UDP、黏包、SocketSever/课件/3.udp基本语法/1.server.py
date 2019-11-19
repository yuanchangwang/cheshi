import socket
# 创建对象 socket.SOCK_DGRAM 代表udp协议
sk = socket.socket(type=socket.SOCK_DGRAM)
# 在网络中注册该主机
sk.bind( ("127.0.0.1",9000) )


# udp服务器,第一次启动时,一定是先接收数据,在发送数据
msg,cli_addr = sk.recvfrom(1024)
print(msg.decode("utf-8"))
print(cli_addr)  #('127.0.0.1', 62464)

# 关闭udp连接
sk.close()