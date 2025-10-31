# Programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.
numero = int(input('Digite um número inteiro: '))
if type(numero) == int:
    print('Este número é inteiro.')
else:
    ('Esse número não é inteiro.')

sucessor = numero + 1
antecessor = numero - 1

print(f'O sucessor de {numero} é {sucessor},' \
f' e o antecessor de {numero} é {antecessor}')