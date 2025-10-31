# Verificando primeira e última ocorrência de uma string
frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A apareceu {frase.count('A')} vezes na frase.') # --> .count('A') conta quantas letras A apareceram dentro da frase 
print(f'A primeira letra A apareceu na posição {frase.find('A')+1}') # --> .find('A') conta o índice da posição em que apareceu a primeira letra A
print(f'A última letra A apareceu na posição {frase.rfind('A')+1}') # --> rfind('A') conta a primeira letra A da DIREITA pra esquerda