# PROCURANDO UMA STRING DENTRO DE OUTRA

nome = str(input('Digite seu nome completo: ')).strip()
if 'silva' in nome:
    print('Você faz parte da família SILVA')
else:
    print(f'Prazer em conhecer você, {nome} !')