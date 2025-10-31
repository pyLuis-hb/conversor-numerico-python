# Primeiro e último nome de uma pessoa

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split() # --> .split() vai fazer uma divisão dentro da string entre espaços, refazendo os índices da str a cada espaço da frase colocando em uma lista
print(f'{n}, é um prazer te conhecer!')
print(f'Seu primeiro nome é {nome[0]}') # --> acessa o primeiro índice exibindo na tela 
print(f'Seu último nome é {nome[len(nome)-1]}') # --> esse -1 vai ler o nome e por ex: 'Luis Felipe Silva' tem 3, então vai de 0 até 2, então tem um a menos.