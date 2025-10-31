from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
consseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem o COSSENO de {consseno:.2f}')
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')