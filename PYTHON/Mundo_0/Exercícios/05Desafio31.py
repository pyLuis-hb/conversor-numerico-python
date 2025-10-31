distancia = float(input('Qual a distância da sua viagem? '))
print('-=-'* 15)
print(f'Você está prestes a começar uma viagem de {distancia} Km.')
preço_200Km = distancia * 0.50
preco_viagens_Longas = distancia * 0.45

if distancia <= 200:
    print(f'O custo desta viagem ficará em torno de R${preço_200Km:.2f} !')
else:
    print(f'O custo dessa viagem por ser mais longa, ficará em torno de R${preco_viagens_Longas:.2f} !')