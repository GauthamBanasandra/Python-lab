from socket import *

__author__ = 'gauth_000'

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('192.168.0.3', 12002))
while True:
    client_socket.send(str(input()).encode('utf-8'))
    print(client_socket.recv(1024).decode())
client_socket.close()