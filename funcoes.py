def resposta():
    # Retorna o nome digitado pelo usuario
    resp = input('>: ')
    resp = resp.lower()
    resp = resp.replace('é','eh')
    return resp

def pegaNome(nome):
    if 'o meu nome eh ' in nome:
        nome = nome[14:]
        
    nome = nome.title()
    return nome

def respondeNome(nome):
    conhecidos = ['Raimundo', 'Will', 'Joao']
    frase = 'Muito prazer '
    for conhecido in conhecidos:
        #print(conhecido)
        if nome == conhecido:
            frase = 'Olá '        
    return frase+nome