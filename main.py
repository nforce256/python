from funcoes import *
print('Olá, qual o seu nome?')    
nome = pegaNome(resposta())
resp = respondeNome(nome)
print(resp)
while True:
    rpst = input('>: ')
    if rpst == 'tchau':
        break
    else:
        print('Digite outra coisa ')
        
print('Até mais!')