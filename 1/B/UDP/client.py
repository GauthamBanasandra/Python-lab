from socket import *
import json

__author__ = 'gauth_000'


def send_recv_msg(*msg):
    sock.sendto(json.dumps(msg).encode(), ('127.0.0.1', 12000))
    print(sock.recvfrom(('127.0.0.1', 12000)).decode())


sock = socket(AF_INET, SOCK_DGRAM)
# send_recv_msg('reverse this string', 'rev')
# send_recv_msg('capitalize this string', 'cap')
send_recv_msg('encrypt this string', 'encr')
sock.close()