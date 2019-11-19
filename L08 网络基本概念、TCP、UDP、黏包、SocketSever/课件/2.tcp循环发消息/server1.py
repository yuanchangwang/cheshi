import socket
sk = socket.socket()
# 注册主机
sk.bind( ("127.0.0.1",9000) ) # 参数是元组
# 开启监听
sk.listen()
# 三次握手
# conn,addr = sk.accept()

'''
conn:
<socket.socket fd=480, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9000), raddr=('127.0.0.1', 60879)>
addr:
('127.0.0.1', 60879)
'''
# print(conn,addr)

while True:
	conn,addr = sk.accept()
	while True:
		msg = conn.recv(1024)
		print(msg.decode("utf-8"))
		# 服务器发消息
		message = input("我要发的数据:>>>")
		conn.send(message.encode("utf-8"))
		if message == "q":
			break

# 四次挥手
conn.close()
# 退还端口
sk.close()


