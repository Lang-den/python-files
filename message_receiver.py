import socket

host = ''
port = 4500
buffer = ''
addr = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(addr)
sock.listen(1)
conn, sender = sock.accept()
print(conn, sender)


while True:
    data = conn.recv(buffer)
    if not data: 
        break
    print(data)

conn.close()

