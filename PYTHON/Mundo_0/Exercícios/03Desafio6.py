# Algoritmo que le um número e mostra o seu dobro, triplo e raiz quadrada

numero = int(input('Escolha um número: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** 0.5


print(f'O dobro de {numero} é: {dobro}')
print(f'O triplo de {numero} é: {triplo}')
print(f'A raiz quadrada de {numero} é: {raiz_quadrada:.2f}')