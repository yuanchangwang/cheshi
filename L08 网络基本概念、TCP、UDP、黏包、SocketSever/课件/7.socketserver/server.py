# 服务器
import socketserver
import socket
class MyServer(socketserver.BaseRequestHandler):
	def handle(self):
		# 自定义的逻辑...
		print("----> 执行这句话")
		print(self.request)
		print(self.client_address)
		# pass
		
# 生成一个对象
# ThreadingTCPServer( "ip端口号" ,"自定义的类"  )
server = socketserver.ThreadingTCPServer( ("127.0.0.1",9000) , MyServer )
# 循环调用
server.serve_forever()

