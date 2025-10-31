# Sorteando uma ordem na lista
from random import shuffle
alunos = [
    'Luis', 'Tereza', 'José', 'Thiago', 'Cibele'
]
shuffle(alunos) # ---> shuffle(alunos) embaralha a lista aleatoriamente.
print('A ordem de apresentação será')
print('-' * 30)

for i in range(5): # --> range(5) gera os números de 0 a 4, e com i + 1 exibimos de 1 a 5.
    print(f'{i + 1} - {alunos[i]}') # --> alunos[i] acessa o aluno correspondente àquela posição.

print('-' * 30)
