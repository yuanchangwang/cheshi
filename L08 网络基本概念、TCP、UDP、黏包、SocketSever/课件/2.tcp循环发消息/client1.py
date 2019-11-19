import socket
sk = socket.socket()
sk.connect( ("127.0.0.1",9000) )


while True:
	message = input(">>>:")
	sk.send(message.encode("utf-8"))
	# 接收服务器发过的消息
	res = sk.recv(1024)
	if res == b"q":
		break
	
	print(res.decode("utf"))
sk.close()


