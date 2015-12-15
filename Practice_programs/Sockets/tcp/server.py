from socket import *

__author__ = 'gauth_000'

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', 12000))
server_socket.listen(1)
print('Waiting for the client to connect')
connection_socket, address = server_socket.accept()
while True:
    message = connection_socket.recv(1024)
    print(address, ':', message)
    connection_socket.send(message.upper())
connection_socket.close()
