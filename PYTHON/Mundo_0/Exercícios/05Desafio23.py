
numero = int(input('Informe um número: '))
unidade = numero // 1 % 10
dezena = numero //10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f' Analisan o número {numero}')
print('-' *20)
print(f'Unidade: {unidade}', 
f'Dezena: {dezena}', 
f'Centena: {centena}', 
f'Milhar: {milhar}',
)
      