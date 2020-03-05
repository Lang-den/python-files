import socket

ip_address = '10.61.58.200'
port = 4501
buffer = 1024
message = 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_address, port))
s.send(message.encode())

s.close()

