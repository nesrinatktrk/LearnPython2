import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mesaj=b"selam"
ip="192.168.2.56"
port=4444
s.connect((ip,port))
s.send(mesaj)
