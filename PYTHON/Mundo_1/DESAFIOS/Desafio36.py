print('-=-' * 9)
print('SIMULADOR DE EMPRÉSTIMOS')
print('-=-' * 9)

imovel = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual é o seu salário? R$'))
tempo = int(input('Em quantos anos deseja financiar o imóvel? '))

# Converter anos em meses
parcelas = tempo * 12

# Valor de cada parcela
valor_parcela = imovel / parcelas

# Limite máximo de parcela (30% do salário)
limite = salario * 0.30

print('-=-' * 9)
print(f'Valor do imóvel: R${imovel:.2f}')
print(f'Tempo de financiamento: {tempo} anos ({parcelas} meses)')
print(f'Parcela mensal estimada: R${valor_parcela:.2f}')
print(f'Limite permitido (30% do salário): R${limite:.2f}')
print('-=-' * 9)

if valor_parcela <= limite:
    print('✅ PARABÉNS! Seu financiamento foi aprovado.')
else:
    print('❌ EMPRÉSTIMO NEGADO. O valor da parcela excede 30% do seu salário.')
