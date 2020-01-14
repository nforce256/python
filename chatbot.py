print('Olá, qual o seu nome?')
nome = input('>: ')
conhecidos = ['Raimundo', 'Will', 'Joao']
for conhecido in conhecidos:
    if nome == 'Adriano':
        print('Olá ' + nome)
    else:
        print('Muito prazer ' + nome)
while True:
    resposta = input('>: ')
    if resposta == 'tchau':
        break
    else:
        print('Digite outra coisa ')
        
print('Até mais!')