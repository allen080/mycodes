import time
alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encriptar(string,base):
    global alpha
    lista_chr=alpha[base:]
    lista_chr_finais=alpha[:base]; lista_chr.extend(lista_chr_finais)
    string_encriptada=''
    
    alpha_up=[]
    lista_chr_up=[]
    for i in alpha:
        alpha_up.append(i.upper())
    for j in lista_chr:
        lista_chr_up.append(j.upper())
    
    for caracter in string:
        if caracter in lista_chr:
            string_encriptada+=lista_chr[alpha.index(caracter)]
        elif caracter in alpha_up:
            string_encriptada+=lista_chr_up[alpha_up.index(caracter)]
        else:
            string_encriptada+=caracter
    print('\nstring em ROT%i:'%base)        
    print(string_encriptada)
    
def decriptar(string,base):
    global alpha
    lista_chr=alpha[base:]
    lista_chr_finais=alpha[:base]; lista_chr.extend(lista_chr_finais)
    string_decriptada=''
    
    alpha_up=[]
    lista_chr_up=[]
    for i in alpha:
        alpha_up.append(i.upper())
    for j in lista_chr:
        lista_chr_up.append(j.upper())
        
    for caracter in string:
        if caracter in lista_chr:
            string_decriptada+=alpha[lista_chr.index(caracter)]
        elif caracter in alpha_up:
            string_decriptada+=alpha_up[lista_chr_up.index(caracter)]
        else:
            string_decriptada+=caracter
    print('\nstring decriptada em ROT%i:'%base)
    print(string_decriptada)    

print('Caesar shift decoder\n')
print('0: Sair')
print('1: Criptografar a string')
print('2: Decriptar a string')
metodo = input('\nmetodo: ')
while metodo<'0' or metodo>'2':
    print('digite um dos metodos acima.')
    metodo = input('metodo: ')

if metodo=='0':
    print('Saindo do programa...'); time.sleep(1.5); exit()

try:
    string=input('\nstring: ')
    base_ale = input('usar todas as bases?(s=sim/n=nao): ')    

    if base_ale.lower().startswith('s'):
        base_ale='all'
    else:
        base=int(input('base: '))        
        while base<0 or base>25:
            print('digite uma base entre 0 e 25')
            base=int(input('base: '))
except:
    print('erro! saindo do programa...'); time.sleep(1.5); exit()

if base_ale=='all':
    if metodo=='1':
        for base in range(26):
            encriptar(string,base)
    if metodo=='2':
        for base in range(26):
            decriptar(string,base)
    
elif metodo=='1':
    encriptar(string,base)
elif metodo=='2':
    decriptar(string,base)

time.sleep(50)
