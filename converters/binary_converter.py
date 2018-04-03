import time
binarios = {'00100000':' ','00001':'a','00010':'b','00011':'c','00100':'d','00101':'e','00110':'f','00111':'g','01000':'h','01001':'i','01010':'j','01011':'k','01100':'l','01101':'m','01110':'n','01111':'o','10000':'p','10001':'q','10010':'r','10011':'s','10100':'t','10101':'u','10110':'v','10111':'w','11000':'x','11001':'y','11010':'z','00110000':'0','00110001':'1','00110010':'2','00110011':'3','00110100':'4','00110101':'5','00110110':'6','00110111':'7','00111000':'8','00111001':'9','01000000':'@','01111011':'{','01111100':'|','01111101':'}','01111110':'~','00100001':'!','00100011':'#','00100100':'$','00100101':'%','00100110':'&','00100111':'\'','00101000':'(','00101001':')','00101010':'*','00101011':'+','00101100':',','00101101':'-','00101110':'.','00101111':'/','00111010':':','00111011':';','00111100':'<','00111101':'=','00111110':'>','00111111':'?','11000011 10101001':'é','11000011 10000111':'ç'}

def reverse_binary(binarios):
#Inverter o dicionario de binarios onde o texto sao as chaves e os binarios sao as keys e os pedestres sao os banhistas.
    ascii_binary = '{'
    for i in range(0,len(binarios)):
        ascii_binary+='"'+str(list(binarios.items())[i][1])+'"'':'+'"'+str(list(binarios.items())[i][0])+'"'+','
    ascii_binary+='}'
    ascii_binary=eval(str(ascii_binary))
    return ascii_binary

def convert_to_ascii(converter):
#converter a string de binarios para ascii text
    global binarios
    binario_convertido=''; cont=0
    if ' ' not in converter:
        converter2=''
        try:
            for i in range(len(converter)//8):
                converter2+=converter[cont:cont+8]+' '
                cont+=8
            converter2=converter2.rstrip(); converter2=converter2.lstrip()
            converter=converter2
        except:
            print('erro!'); time.sleep(1.5); exit()
    lista_binarios = converter.split()
    for binario_num in lista_binarios:
        
        if binario_num.startswith('010'):
            binario_convertido+=binarios[binario_num[3:]].upper()
        elif binario_num.startswith('011'):
            binario_convertido+=binarios[binario_num[3:]].lower()
        elif binario_num in binarios:
            binario_convertido+=binarios[binario_num]
        elif binario_num == '00100010':
            binario_convertido+='"'
        else:
            binario_convertido+='NULL'        
    return binario_convertido

def convert_to_binary(converter_texto):
#converter o texto para numeros binarios
    global ascii_binary
    texto_convertido=''
    texto_lista=[]
    for i in converter_texto:
        texto_lista.append(i)

    for ascii_var in texto_lista:
        if ascii_var=='"':
            texto_convertido+='00100010'
        elif 'a' <= ascii_var <= 'z':
            texto_convertido+='011'+ascii_binary.get(ascii_var)
        elif 'A' <= ascii_var <= 'Z':
            texto_convertido+='010'+ascii_binary.get(ascii_var.lower())
        elif ascii_var in ascii_binary:
            texto_convertido+=ascii_binary[ascii_var]
        else:
            texto_convertido+='NULL'
        texto_convertido+=' '
    return texto_convertido

#inicio do programa
print('Binary converter\n')
print('0: Sair')
print('1: Binario para ASCII(Texto)')
print('2: ASCII para Binario\n')
metodo = input('qual metodo vc deseja utilizar?: ')

while metodo != '1' and metodo != '2' and metodo != '0':
    print('erro. digite o índice de um dos metodos ou "0" para sair')
    metodo = input('qual metodo vc deseja utilizar?: ')

if metodo == '0':
    print('Encerrando o programa.')
    time.sleep(2)
    exit()

if metodo == '1':
    converter = input('binarios: ')
    #try:
    convertido=convert_to_ascii(converter)
    #except:
    #print('erro!')
    #time.sleep(1); exit()
    print('\nBinarios convertidos:',convertido)

if metodo == '2':
    converter_texto = input('texto: ')
    try:
        ascii_binary=reverse_binary(binarios)
        texto_convertido=convert_to_binary(converter_texto)
    except:
        print('erro!')
        time.sleep(1)
    print('\nTexto convertido: ',texto_convertido)

time.sleep(15)
