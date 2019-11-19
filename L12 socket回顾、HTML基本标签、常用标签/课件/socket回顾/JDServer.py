

import socket

sock=socket.socket()
sock.bind(("127.0.0.1",8800))
sock.listen(5)

while 1:
    conn,addr=sock.accept()
    data=conn.recv(1024)
    print("data",data)
    with open("jd.html","rb") as f:
        data=f.read()
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n"+data)