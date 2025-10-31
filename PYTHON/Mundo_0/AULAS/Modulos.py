from math import sqrt, ceil # importou apenas essas duas funcionalidades
numero = int(input('Digite um número: '))
raiz = sqrt(numero)
print('A raiz de {} é igual a {}'.format(numero, ceil(raiz))) # math.ceil(raiz) arredondou de 9.0 para 9