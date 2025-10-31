dias = int(input('Por quantos dias foram alugados o carro?: '))
km = float(input('Quantos Km foram rodados?: '))
pago = (dias * 60) + (km * 0.15)

print(f'O total apagar pelo aluguel do veículo é de R${pago:.2f}')