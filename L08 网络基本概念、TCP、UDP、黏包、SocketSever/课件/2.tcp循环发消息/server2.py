# 服务器
import socketserver
import socket
class MyServer(socketserver.BaseRequestHandler):
	def handle(self):
		# 自定义的逻辑...
		print("----> 执行这句话")
		# print(self.request)
		# print(self.client_address)
		conn = self.request
		while True:
			# 接收消息
			msg = conn.recv(1024)
			print(msg.decode("utf-8"))
			# pass
			
			conn.send(b'world')
		
# 生成一个对象
# ThreadingTCPServer( "ip端口号" ,"自定义的类"  )
server = socketserver.ThreadingTCPServer( ("127.0.0.1",9000) , MyServer )
# 循环调用
server.serve_forever()

'''
try:
    # lst = [1, 2, 3]
    # print(lst[99])
    print(333)
finally:
    print(1)
    print(2)
'''

"""
try .. finally ..
不论try 代码块里面的代码是不是报错,
都会执行finally这个代码块中的内容.
作用:正常情况,如果报错,后面的代码一律不执行,
但是特殊条件下,又必须在报错的行为中,执行某些代码,
那么这样的代码加到finally当中
"""

