print('-=-' * 15)
print('Analisador de Triângulos')
print('-=-' * 15)

a = float(input('Primeiro Seguimento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

''' Fórmula é se a soma entre dois lados forem maior que o terceiro lado, PODEM FORMAR triângulo
 Se for menor. não podem formar um triângulo'''
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos PODEM FORMAR um triângulo!')
else:
    print('Os seguimentos NÃO PODEM FORMAR triângulo')
