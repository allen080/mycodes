#!/usr/bin/python
from scapy.all import *

def capture(packet):
	if packet[TCP].payload:
		data = str(packet[TCP].payload)
		
		if data.startswith('POST') and '&' in data:
			data_cont = data.split()
			print
			
			for content in data_cont:
				if 'host' in content.lower(): 
					print('host: '+data_cont[data_cont.index(content)+1])
			print('\033[1;31m'+(data.split()[-1].replace('&','\n')).replace('=',': ')+'\033[0;0m')

print('[*] sniffing...')
sniff(filter='port 80',store=0,prn=capture)
