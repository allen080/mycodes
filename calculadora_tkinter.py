import tkinter
from functools import partial

class Calculator(object):
    def __init__(self, tela):
        #fontes:
        self.font=('Verdana','10','bold')
        
        #frames:
        self.frame1 = tkinter.Frame(tela) #frame checkbuttons
        self.frame2 = tkinter.Frame(tela) #frame texto
        self.frame3 = tkinter.Frame(tela,bg='snow2') #frame botao calcular
        self.frame4 = tkinter.Frame(tela,pady=10,bg='snow2') #frame do texto das formulas
        self.frame5 = tkinter.Frame(tela) #frame da tupla de botoes
        
        self.frame1.pack(); self.frame2.pack(); self.frame3.pack(); self.frame4.pack()
        self.frame5.pack()
        
        #logo:
        self.image = tkinter.Label(self.frame1); self.image['image']=logo
        self.image.pack()

        #checkbuttons:
        self.botao_selecionar = False
        self.botao_padrao = tkinter.Checkbutton(self.frame2,text='Calculadora Padrão',bg='snow2',font=self.font,width=18,command=self.ativa_botao)
        self.botao_padrao.pack(side='left')
        
        self.botao_selecionar2 = False
        self.botao_cient = tkinter.Checkbutton(self.frame2,text="Calculadora Científica",bg='snow2',font=self.font,width=18,command=self.ativa_cient)
        self.botao_cient.pack()

        #entry
        self.entry = tkinter.Entry(self.frame3,width=70)
        self.entry.pack()

        #botao calcular
        self.botao_calcular = tkinter.Button(self.frame3,text='Calcule',bg='ivory3',font = self.font,width=18,pady=4,command=self.calcular)
        self.botao_calcular.pack()
        
        self.resultado = tkinter.Label(self.frame4,text='Resultado',bg='snow2',font=self.font,fg='midnight blue')
        self.resultado.pack()

        #botoes calculos:
        botoes = ('Soma(x,y)','Subtrair(x,y)','Mult(x,y)','Div(x,y)','Div_Int(x,y)','Exp(x,y)','Sqrt(x)')
        for b in range(len(botoes)):
            if b%3==0:
                subframe = tkinter.Frame(self.frame5,bg='snow2')
                subframe.pack(side='top')
                
            botao = tkinter.Button(subframe,text=botoes[b],bg='forest green',fg='black',width=25,padx=5,pady=4,font=self.font, command = partial(self.Colocatexto,botoes[b]))
            botao.pack(side = 'left')
        self.botao_del = tkinter.Button(subframe,text='Del',font=self.font,bg='red',width=25,padx=5,pady=4,command=self.Deletatexto)
        self.botao_del.pack()

    def Colocatexto(self,text):
        self.entry.insert('end',text)

    def Deletatexto(self):
        self.entry.delete(0,'end')
        
    def Msg(self,text,cor='red'):
        self.resultado['text']=text
        self.resultado['fg']=cor
        
    def calcular(self):
        entrada=self.entry.get()
        if entrada.startswith('Soma'):
            self.Msg(entrada+' = %s'%str(float(entrada[5:entrada.index(',')])+float(entrada[entrada.index(',')+1:entrada.index(')')])),'green')
        elif entrada.startswith('Sub'):
            self.Msg(entrada+' = %s'%str(float(entrada[9:entrada.index(',')])-float(entrada[entrada.index(',')+1:entrada.index(')')])),'green')
        elif entrada.startswith('Mult'):
            self.Msg(entrada+' = %s'%str(float(entrada[5:entrada.index(',')])*float(entrada[entrada.index(',')+1:entrada.index(')')])),'green')
        elif entrada.startswith('Div('):
            self.Msg(entrada+' = %s'%str(float(entrada[4:entrada.index(',')])/float(entrada[entrada.index(',')+1:entrada.index(')')])),'green')
        elif entrada.startswith('Div_Int'):
            self.Msg(entrada+' = %s'%str(float(entrada[8:entrada.index(',')])//float(entrada[entrada.index(',')+1:entrada.index(')')])),'green')
        elif entrada.startswith('Exp'):
            self.Msg(entrada+' = %s'%str(float(entrada[4:entrada.index(',')])**float(entrada[entrada.index(',')+1:entrada.index(')')])),'green')
        elif entrada.startswith('Sqrt'):
            self.Msg(entrada+' = %s'%str(float(entrada[5:entrada.index(')')])**(1/2)),'green')
        else:
            self.Msg('Não foi possivel realizar a conta. Escolha uma das opçoes abaixo')
                    
        self.Deletatexto()
        
    
    def ativa_botao(self):
        self.botao_selecionar = not self.botao_selecionar
        if self.botao_selecionar:
            self.Msg('Calculadora Padrão ativada')
            if self.botao_selecionar2:
                self.botao_selecionar2=False
                self.botao_cient.deselect()
        else:
            self.Msg('Calculadora Padrão desativada')

    def ativa_cient(self):
        self.botao_selecionar2 = not self.botao_selecionar2
        if self.botao_selecionar2:
            if self.botao_selecionar:
                self.botao_selecionar=False
                self.botao_padrao.deselect()
            self.Msg('Calculadora Científica nao pode ser exibida')

tela = tkinter.Tk()
logo = tkinter.PhotoImage(file='logo_calculator.gif')
Calculator(tela)

tela.geometry('800x600')
tela.title('Calculadora')
tela['bg']='snow2'

tela.mainloop()
