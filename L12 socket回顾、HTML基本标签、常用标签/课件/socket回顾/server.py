import socket

sock=socket.socket()
sock.bind(("127.0.0.1",8800))
sock.listen(5)


while 1 :
    conn, addr = sock.accept()
    while 1:
        data = conn.recv(1024)
        print("data:", data.decode())
        if data.decode()=="q":break
        res = input("想应 >>>")
        conn.send(res.encode())