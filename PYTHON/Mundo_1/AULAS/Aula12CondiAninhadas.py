nome = str(input('Qual é seu nome? '))
if nome == 'Luis':
    print(f'Que belo nome !')
elif nome == 'João' or nome == 'Maria' or nome == 'Gabriel':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome} !')