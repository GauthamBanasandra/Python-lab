import json
from socket import *

__author__ = 'gauth_000'


def perform_operation(msg):
    if msg[1] == 'rev':
        send_msg = msg[0][::-1]
    elif msg[1] == 'cap':
        send_msg = msg[0].upper()
    elif msg[1] == 'encr':
        send_msg = ''.join(map(lambda x: chr(ord(x) + 1), str(msg[0])))
    else:
        send_msg = 'invalid operation'
    return send_msg


sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', 12000))
msg=sock.recv(1024)
print(msg)
sock.close()