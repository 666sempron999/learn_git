import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("", 10000))
s.bind(("", 10000))
s.bind(("", 10000))
s.bind(("", 10000))
s.listen(1)
s.listen(1)
s.listen(1)
s.listen(1)

connection, address = s.accept()

print("message : {}".format(connection.recv(1024).decode()))
print("from {}".format(address))

