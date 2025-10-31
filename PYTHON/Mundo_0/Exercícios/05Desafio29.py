# RADAR ELETRÔNICO

velocidade = float(input('Qual é a velocidade atual do veículo? '))
limite_via = 80
multa = (velocidade-80) * 7 # --> (velocidade-80) está tirando o excedente que é 80km/h do limite da vida.
if velocidade > limite_via:
    print(f'MULTADO! Você excedeu o limite da via que é de {limite_via}Km/h.')
    print(f'Você pagara uma multa no valor de R${multa:.2f} reais')
    if velocidade < 40:
        print('MULTADO! Você está abaixo da metado do limite da via.')
        print(f'Você pagara uma multa no valor de R${multa:.2f} reais')
else:
    print('Tenha um ótimo dia! Dirija sempre com segurança.')