
import socket

sock=socket.socket()
sock.connect(("127.0.0.1",8800))

while 1:
    data=input(">>>")
    sock.send(data.encode())
    res=sock.recv(1024)
    print(res.decode())


