#!/usr/bin/python
import argparse
import os
from socket import *

parser = argparse.ArgumentParser(description="Simple Python Portscanner.")

parser.add_argument('host',help="ip to scan",type=str)
parser.add_argument('-p','--ports',help="ports to scan (default 0-1024)",action='store')

host = parser.parse_args().host
if parser.parse_args().ports:
	ports = parser.parse_args().ports.split(',')
else:
	ports = range(1,1025)

def define_sock():
	scan = socket(AF_INET,SOCK_STREAM)
	scan.settimeout(0.22)
	return scan

try:
	for port in ports:
		scan = define_sock()

		code = scan.connect_ex((host,int(port)))
		if code == 0:
			print "open-> %s"%port

		elif parser.parse_args().ports:
			print "closed-> %s"%port	

		elif port%200==0:
			print '[*] scanning %s:%s'%(host,port)	
except Exception as error:
	raise Exception(error)
