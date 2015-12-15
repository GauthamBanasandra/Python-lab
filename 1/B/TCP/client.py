from socket import *
import json

__author__ = 'gauth_000'


def send_recv_msg(*msg):
    sock.send(json.dumps(msg).encode())
    print(sock.recv(1024).decode())


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('127.0.0.1', 12000))
# send_recv_msg('reverse this string', 'rev')
# send_recv_msg('capitalize this string', 'cap')
send_recv_msg('encrypt this string', 'encr')
sock.close()
