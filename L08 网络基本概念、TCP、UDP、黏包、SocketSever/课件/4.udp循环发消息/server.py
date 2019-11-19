# ### udp 服务器 循环发消息
import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
# 把该主机注册到网络,让其他主机可以找到
sk.bind( ("127.0.0.1",9000) )

while True:
	# 同一时间最大接收1024个字节
	msg,cli_addr = sk.recvfrom(1024)
	print(msg.decode("utf-8"))
	print(cli_addr)
	
	message = input("请输入发送的数据哦>>>")
	sk.sendto(message.encode("utf-8"),cli_addr)
	
sk.close()