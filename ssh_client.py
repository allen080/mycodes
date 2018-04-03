import paramiko
import os
from time import sleep
from getpass import getpass

if len(os.sys.argv) > 1:
	host=os.sys.argv[1]
else:
	host=raw_input('server: ')

user = raw_input('user: ')
password = getpass('password: ')

print('\nconnecting...'); sleep(1)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
	ssh.connect(host,username=user,password=password,timeout=5)
	print "connected to %s@%s\n"%(user,host)
except Exception as e:
	print "error: "+str(e)
	ssh.close(); exit()

if user=='root':
	perm='#'
else:
	perm='$'

while True:	
	try:
		execute = raw_input('%s@%s:~%s '%(user,host,perm))
		if execute == 'exit':
			break
		elif execute == 'clear':
			os.system('cls')
			continue

		entry,out,errors = ssh.exec_command(execute)

		out,errors = out.readlines(),errors.readlines()

	except Exception as er:
		print "error: "+str(er)
		continue

	if len(out)>0:
		for o in out:
			print(o.strip())
	elif len(errors)>0:
		for e in errors:
			print(e.strip())

ssh.close()