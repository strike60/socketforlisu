import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 1234))

s.send('1'.encode('utf-8'))
print(s.recv(1024))
s.close()