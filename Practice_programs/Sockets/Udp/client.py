from socket import *
__author__ = 'gauth_000'
sock=socket(AF_INET, SOCK_DGRAM)
sock.sendto(b'udp message', ('192.168.0.3', 12002))