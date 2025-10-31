from random import choice
from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

numero_escolhido = randint(0,5) # --> Gera um número inteiro aleatório de 0 a 5
tentativas = 3 #Definição de tentativas para o usuário acertar

# Laço para enquanto houver tentavias o jogo continua
while tentativas > 0:
    try:  # Tenta executar o bloco de código abaixo; caso ocorra erro, vai para o 'except'
        escolha = int(input('Em que número eu pensei? '))

        # Validação: impede que o usuário digite números fora do intervalo permitido
        if escolha < 0 or escolha >5:
            print('Entrada inválida. Digite apenas um número entre 0 e 5.')
            continue

        print('PROCESSANDO...')
        sleep(1.5)

        # Verifica se o número digitado é igual ao número sorteado
        if escolha == numero_escolhido:
            print('Você acertou, parabens!')
            break
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f'Você errou! Tentativas restantes: {tentativas}')
            else:
                print(f'Você perdeu! O número era {numero_escolhido}')   
    except ValueError: # Captura erro se o usuário digitar algo que não seja número inteiro
        print('Entrada inválida. Digite apenas número!')
