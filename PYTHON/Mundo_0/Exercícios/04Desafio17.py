from math import hypot
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente) # Formula: (cateto oposto **2 + cateto adjacente **2) ** (1/2)-->Meio

print(f'A hipotenusa vai medir {hipotenusa:.2f}')