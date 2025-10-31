a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', a.isspace())
print('É numérico? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('Está maiúscula? ', a.isupper())
print('Está em minúscula? ', a.islower())
print('Está capitalizada? ', a.istitle())
# Capitalizada é quando o primeiro caractere de uma string está maiúsculo e todos os outros caracteres estão minúsculo. 
