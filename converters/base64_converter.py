import base64
import time

def main():
	print("Base64 Converter\n")
	print("0: Sair\n1: Base64 para texto\n2: Texto para Base64\n")
	while True:
		op = input('opção: ')
		if op == "1" or op == "2" or op == "0":
			break
		print("escolha uma das opções acima.")

	if op == "0":
		print("saindo..."); time.sleep(1); return
	try:
		convert = input('\nConverter: ')
		if op == "2":
			print("\nConvertido: %s"%base64.encodestring(convert.encode()).decode().strip())
		else:
			print("\nConvertido: %s"%base64.decodestring(convert.encode()).decode().strip())
	except Exception as err:
		print("erro:",err)

if __name__=='__main__':
	main()