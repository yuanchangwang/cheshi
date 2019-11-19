# 客户端
import socket
sk = socket.socket()
sk.connect( ("127.0.0.1",9000) )

while True:
	# 发消息
	sk.send(b"hello")
	
	# 接收服务器消息
	msg = sk.recv(1024)
	print(msg.decode("utf-8"))


sk.close()