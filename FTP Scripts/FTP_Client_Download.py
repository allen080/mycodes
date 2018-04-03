#!C:\python34\python.exe
import ftplib
import os

#host = '127.0.0.1'
while True:
	host = input('Ftp server: ')
	if host=='':
		continue
	port = input('Port(default=21): ')
	
	if port == '':
		port = 21
	if host != '':
		port=int(port)
		break	

print ('\n[*] tentando se conectar...')
try:
	client = ftplib.FTP()
	client.connect(host,port)
	client.login()
except Exception as er:
	print ('erro:',str(er))
	exit()

print('[*] host conectado com sucesso.\n')

temp = os.sys.stdout
os.sys.stdout = open('sys_stdout.txt','w')

client.retrlines('LIST')

os.sys.stdout = temp
files_server = [linha.split()[-1] for linha in open('sys_stdout.txt').readlines()]

os.system('del sys_stdout.txt')

print('Arquivos:')
for file in range(len(files_server)):
	print('%i: %s'%(file,files_server[file]))

print()

while True:
	comando = input('Download(digite "all" para todos ou "exit" para sair): ')
	
	if comando == 'all':
		for arq in files_server:
			print('[*] downloading %s...'%arq)
			with open(arq,'wb') as file_download:
				client.retrbinary('RETR '+arq, file_download.write, 1024)

		out = input('\ndownloads concluidos! sair? (s=sim/n=nao): ')
		if out.startswith('s'):
			break
		else:
			continue

	elif comando == 'exit':
		print('saindo...'); break
	else:
		try:
			comando = int(comando)
		except:
			print('digite o numero do indice do arquivo para baixar.')
			continue

	if comando in range(len(files_server)):
		print('\n[*] fazendo download de %s'%files_server[comando])
		
		with open(files_server[comando],'wb') as file_download:
			client.retrbinary('RETR '+files_server[comando], file_download.write, 1024)
		print('[*] download concluido.\n')

	else:
		print('[!] arquivo nao encontrado.')
