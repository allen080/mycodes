try:
	from tkinter import *
	from bitcoin_cotacao_script import cotacao_btc
	from dolar_cotacao_script import cotacao_dolar
except ImportError as erro:
	print("Erro de importação: ",erro); input();exit()

class cotacao():
	def __init__(self):
		self.root=Tk()
		self.root.title('Cotação Atual')
		self.root.resizable(False,False)

		self.font=("Verdana",'10','bold')

		self.frame_botoes=Frame(self.root)
		self.frame_valores=Frame(self.root)
		self.frame_botoes.pack(); self.frame_valores.pack()

		self.BTC=Button(self.frame_botoes,text="Bitcoin",width=15,height=2,bg='firebrick2',font=self.font,padx=2,command=self.btc_cotacao)
		self.dolar=Button(self.frame_botoes,text="Dólar",width=15,height=2,bg='royal blue',font=self.font,padx=2,command=self.dolar_cotacao)
		self.BTC.pack(side=LEFT); self.dolar.pack()

		self.btc_packed,self.dolar_packed=False,False

		self.root.mainloop()
	
	def btc_cotacao(self):
		if self.dolar_packed:
			self.dolar_hj.pack_forget()

		if self.btc_packed:
			return
		
		valores_btc = cotacao_btc()
		self.btc_compra=Label(self.frame_valores,text=valores_btc[0],font=self.font,fg='firebrick2')
		self.btc_venda=Label(self.frame_valores,text=valores_btc[1],font=self.font,fg='firebrick2')
		self.btc_compra.pack(); self.btc_venda.pack()
		
		self.btc_packed=True; self.dolar_packed=False

	def dolar_cotacao(self):
		if self.btc_packed:
			self.btc_compra.pack_forget(); self.btc_venda.pack_forget()

		if self.dolar_packed:
			return

		dolar=cotacao_dolar()
		self.dolar_hj=Label(self.frame_valores,text=dolar,font=self.font,fg='royal blue')
		self.dolar_hj.pack()

		self.dolar_packed=True; self.btc_packed=False
		
if __name__=='__main__':
	cotacao()
