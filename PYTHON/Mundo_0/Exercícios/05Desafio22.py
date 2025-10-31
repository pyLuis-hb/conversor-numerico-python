nome = input('Digite seu nome: ').strip() # --> .strip() elimina todos os espaços do inicio e do fim 

def informacao():
    maiusculo = nome.upper() #  --> .upper() formata as letras para MAIÚSCULA
    print(f'Seu nome em maiúsculo é {maiusculo}')
    minusculo = nome.lower() #  --> .lower() formata as letras para minúscula
    print(f'Seu nome em minúsculo é {minusculo}')
    tamanho = len(nome.replace(' ', '')) #  --> len() conta qtd de caracteres e o .replace(' ', '') remove os espaços para o len fazer a contagem apenas dos caracteres.
    print(f'Existem {tamanho} letras em seu nome')
    letras_primeiro_nome = (nome.find(' ')) #   --> .find(' ') encontra a primeira ocorrência, nesse caso, encontra o ESPAÇO no texto
    print(f'Seu primeiro nome tem {letras_primeiro_nome} letras')
    nome_separado = nome.split()
    print(f'Seu primeiro nome é {nome_separado[0]} e ele tem {len(nome_separado[0])} letras! ') #   --> .split() separa os nomes e joga em uma lista permitindo acessar cada elemento através das [] e o indice

informacao()