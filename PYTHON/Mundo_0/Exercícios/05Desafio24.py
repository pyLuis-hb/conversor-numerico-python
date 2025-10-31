# -- VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO --

cidade = str(input('Qual cidade você nasceu?: ').strip()) # --> elimina os espaços
print(cidade[:5].upper() == 'SANTO') # --> .upper() converte o texto para maiúsculo