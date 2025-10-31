def converter_binario(numero):
    n1 = numero
    resto_binario = []

    while n1 > 0:
        quociente = n1 // 2
        resto = n1 % 2
        print(f'{n1} ÷ 2 = {quociente} (resto {resto})')
        resto_binario.append(str(resto))
        n1 = quociente
    binario = ''.join(resto_binario[::-1])
    print(f'\nResultado final em binário: {binario}')
    print('===' *12)

def converter_octal(numero):
    n2 = numero
    resto_octal = []
    while n2 > 0:
        quociente = n2 // 8
        resto = n2 % 8
        print(f'{n2} ÷ 8 = {quociente} (resto {resto})')
        resto_octal.append(str(resto))
        n2 = quociente
    octal = ''.join(resto_octal[::-1])
    print(f'\nResultado final em octal: {octal}')
    print('===' *12)

def converter_hexadecimal(numero):
    n3 = numero
    resto_hexadecimal = []
    # Dicionário com os dígitos hexadecimais
    hex_digitos = '0123456789ABCDEF'

    while n3 > 0:
        quociente = n3 // 16
        resto = n3 % 16
        simbolo = hex_digitos[resto]
        print(f'{n3} ÷ 16 = {quociente} (resto {resto}) → {simbolo}')
        resto_hexadecimal.append(simbolo)
        n3 = quociente
    hexadecimal = ''.join(resto_hexadecimal[::-1])
    print(f'\nResultado final em Hexadecimal: {hexadecimal}')
    print('===' *12)


# ===================
# PROGRAMA PRINCIPAL
#====================
numero = int(input('Digite um número inteiro: '))
print('===' *10)

binario = converter_binario(numero)
octal = converter_octal(numero)
hexadecimal = converter_hexadecimal(numero)

