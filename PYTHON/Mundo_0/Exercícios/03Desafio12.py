# Calculando porcentagem
preco = float(input('Qual o preço do produto? R$'))
preco_desconto = preco - (preco * 5 / 100)
print(f'O produto que custava R${preco:.2f}, na promoção está saindo por R${preco_desconto:.2f}')