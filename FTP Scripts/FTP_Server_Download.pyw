#!C:\Python34\pythonw.exe
import os
import threading
from tkinter import *

def exibir():
	l = Label(root,text=E.get(),fg='red')
	l.pack()

def ftp():
	porta = port.get()
	os.chdir(dir_ftp_e.get())
	os.popen('start python -m pyftpdlib --port=%s'%porta).read()

def ngrok():
	porta = port.get()
	os.popen('start ngrok tcp %s'%porta).read()

root = Tk()
root.geometry('600x300')
root.title('Local Server FTP')
root.resizable(False,False)
root.configure(bg='royal blue')

f_titulo = Frame(root,bg='royal blue'); f_titulo.pack()
titulo = Label(f_titulo,text='FTP Server Download',fg='dark green',bg='royal blue',font=('Verdana',15,'bold'))
titulo.pack()

f_port = Frame(root,width=90,bg='royal blue'); f_port.pack()

p = Label(f_port,text='Port: ',font=('Verdana',8,'bold'),pady=9,bg='royal blue'); p.pack(side=LEFT)
port = Entry(f_port,font=('Verdana',8)); port.pack(side=LEFT)
port.insert('end',21)

f_dir = Frame(root,width=90,bg='royal blue'); f_dir.pack()

dir_ftp = Label(f_dir,text='Diretório: ',font=('Verdana',10,'bold'),pady=10,bg='royal blue'); dir_ftp.pack(side=LEFT)
dir_ftp_e = Entry(f_dir,font=('Verdana',9),width=60); port.pack(side=LEFT); dir_ftp_e.pack(side=LEFT)
dir_ftp_e.insert('end',os.getcwd())

f_buttons = Frame(root); f_buttons.pack()
send = Button(f_buttons,text="Start FTP ",font=('Verdana',10,'bold'),padx=10, borderwidth=4, command=ftp); send.grid(row=1,column=0)
botao_ngrok = Button(f_buttons,text="Start Ngrok",font=('Verdana',10,'bold'),padx=10,borderwidth=4,command=ngrok); botao_ngrok.grid(row=1,column=1)

root.mainloop()