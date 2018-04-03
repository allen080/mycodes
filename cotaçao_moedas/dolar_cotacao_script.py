import requests,json,time

def cotacao_dolar():
	dolar=requests.get('http://api.promasters.net.br/cotacao/v1/valores?moedas=USD&alt=json')
	if dolar.status_code!=200:
		print('erro na requisição da api!'); exit()
	cotacao_dolar=json.loads(dolar.text)
	dolar_cotacao='Dolar Valor atual: %.2fR$'%cotacao_dolar['valores']['USD']['valor']
	return dolar_cotacao

if __name__=='__main__':
	print(cotacao_dolar())
	time.sleep(10)