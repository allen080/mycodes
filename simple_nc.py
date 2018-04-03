#!/usr/bin/python
import socket, sys

if len(sys.argv) != 3:
	print 'use: simple_nc.py "ip" "port"'
	exit()

host,port = sys.argv[1:]

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.settimeout(5)

try:
	client.connect((host,int(port)))
except Exception as er:
	print "error: %s"%str(er)
	exit()

send = ''

while True:
	send_n = raw_input()
	if send_n == '':
		break
	send += send_n

send+='\n'
client.send(send.encode())

print client.recv(1024)