import socket
sk = socket.socket(type=socket.SOCK_DGRAM)

while True:
	message = input("请输入您要发送的消息:")
	# 发消息
	sk.sendto(message.encode("utf-8"),("127.0.0.1",9000))
	
	# 接收数据
	msg,ser_addr = sk.recvfrom(1024)
	print(msg.decode("utf-8"))
	
sk.close()