#!C:\Python34\python.exe
import requests,time

def cotacao_btc(): #retorna a cotação atual do bitcoin
	api_btc=requests.get('https://www.mercadobitcoin.net/api/BTC/ticker/')
	if api_btc.status_code!=200:
		print('erro na requisição da API!'); time.sleep(3);exit()
	dict_api=api_btc.text; dict_api=eval(dict_api)
	compra_value='BTC Valor de compra atual: %.2fR$'%float(dict_api['ticker']['buy'])
	venda_value='BTC Valor de venda atual: %.2fR$'%float(dict_api['ticker']['sell'])
	return compra_value,venda_value

if __name__=='__main__':
        buy,sell=cotacao_btc()
        print(buy); print(sell)
        print('\nValores obtidos em: https://www.mercadobitcoin.com.br')
        time.sleep(3)
